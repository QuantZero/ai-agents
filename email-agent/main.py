import os
import json
from typing import TypedDict

from dotenv import load_dotenv
from imap_tools import MailBox, AND

from langchain.chat_models import init_chat_model
from langchain_core.tools import tool

from langgraph.prebuilt import ToolNode
from langgraph.graph import StateGraph, START, END


# -----------------------------------------------------------
# Load environment variables from .env
# -----------------------------------------------------------
load_dotenv()

IMAP_HOST = os.getenv("IMAP_HOST")
IMAP_USER = os.getenv("IMAP_USER")
IMAP_PASSWORD = os.getenv("IMAP_PASSWORD")
IMAP_FOLDER = "INBOX"

CHAT_MODEL = "qwen3:8b"

# -----------------------------------------------------------
# Define the message state structure used by LangGraph
# -----------------------------------------------------------


class ChatState(TypedDict):
    messages: list


# -----------------------------------------------------------
# Create and return an IMAP connection object
# -----------------------------------------------------------
def connect():
    """
    Creates an IMAP connection with full debug logging.
    Helps diagnose missing env vars, wrong passwords, or Gmail blocking login.
    """

    print("\n[DEBUG] Attempting IMAP login...")
    print(f"[DEBUG] IMAP_HOST: {IMAP_HOST}")
    print(f"[DEBUG] IMAP_USER: {IMAP_USER}")

    # Mask password for safety
    if IMAP_PASSWORD:
        print(f"[DEBUG] IMAP_PASSWORD length: {len(IMAP_PASSWORD)} (masked)")
    else:
        print("[DEBUG] ERROR: IMAP_PASSWORD is EMPTY or NOT LOADED.")
        raise ValueError(
            "IMAP_PASSWORD is empty. Did you load your .env correctly?")

    # Quick validation before login
    if not IMAP_HOST or not IMAP_USER or not IMAP_PASSWORD:
        raise ValueError(
            "[DEBUG] One or more IMAP environment variables are missing.")

    try:
        mailbox = MailBox(IMAP_HOST)
        print("[DEBUG] Connecting to IMAP server...")

        mailbox.login(IMAP_USER, IMAP_PASSWORD, initial_folder=IMAP_FOLDER)

        print("[DEBUG] Login SUCCESSFUL.")
        return mailbox

    except Exception as e:
        print("\n[DEBUG] IMAP LOGIN FAILED.")
        print("[DEBUG] This usually means:")
        print("        1. WRONG password (did you create an App Password?)")
        print("        2. 2FA not enabled")
        print("        3. IMAP not enabled in Gmail settings")
        print("        4. The .env file wasn't loaded properly")
        print("\n[DEBUG] Full exception:")
        print(e)
        raise e


# -----------------------------------------------------------
# TOOL 1: List unread emails
# -----------------------------------------------------------
@tool
def list_unread_emails():
    """
    Return ONLY the most recent unread email.
    This avoids scanning thousands of unread messages.
    Output includes: UID, subject, sender, and date.
    """
    print("List Unread Emails Tool Called")

    # Step 1: Fetch only unread UIDs (very fast)
    with connect() as mb:
        unread_uids = mb.uids(criteria=AND(seen=False))

    if not unread_uids:
        return "You have no unread messages."

    # Step 2: Choose the newest UID
    newest_uid = sorted(unread_uids, key=int)[-1]

    # Step 3: Fetch that one email’s headers
    with connect() as mb:
        mail = next(
            mb.fetch(AND(uid=newest_uid), headers_only=True, mark_seen=False),
            None
        )

    if not mail:
        return "Error fetching the most recent unread email."

    info = {
        "uid": mail.uid,
        "date": mail.date.astimezone().strftime("%Y-%m-%d %H:%M"),
        "subject": mail.subject,
        "from": mail.from_,
    }

    return json.dumps(info)


@tool
def summarize_email(uid):
    """
    Summarize the body of an email given its IMAP UID.
    Returns a short, plain-text summary.
    """
    print("Summarize Email Tool Called on", uid)

    # Fetch the full email
    with connect() as mb:
        mail = next(mb.fetch(AND(uid=uid), mark_seen=False), None)

    if not mail:
        return f"Could not find email with UID {uid}."

    # Use whichever body exists: text first, HTML fallback
    email_body = mail.text or mail.html or ""

    prompt = (
        "Summarize this email concisely:\n\n"
        f"Subject: {mail.subject}\n"
        f"From: {mail.from_}\n"
        f"Date: {mail.date}\n\n"
        f"{email_body}"
    )

    return raw_llm.invoke(prompt).content


# -----------------------------------------------------------
# Initialize LLMs (Ollama local)
# -----------------------------------------------------------

# LLM with tool access
llm = init_chat_model(CHAT_MODEL, model_provider="ollama")
llm = llm.bind_tools([list_unread_emails, summarize_email])

# Raw LLM (no tools)
raw_llm = init_chat_model(CHAT_MODEL, model_provider="ollama")


# -----------------------------------------------------------
# LangGraph: LLM node
# -----------------------------------------------------------
def llm_node(state):
    """
    Sends all messages so far to the LLM.
    Returns updated state including LLM response.
    """
    response = llm.invoke(state["messages"])
    return {"messages": state["messages"] + [response]}


# -----------------------------------------------------------
# Router: decide if LLM wants to call a tool
# -----------------------------------------------------------
def router(state):
    """
    Checks last LLM message.
    If it contains tool calls → route to tools.
    Otherwise → end conversation.
    """
    last_message = state["messages"][-1]
    return "tools" if getattr(last_message, "tool_calls", None) else "end"


# -----------------------------------------------------------
# Wrap LangGraph’s ToolNode so it returns clean messages
# -----------------------------------------------------------
tool_node = ToolNode([list_unread_emails, summarize_email])


def tools_node(state):
    """
    Executes the tool call selected by the LLM.
    Appends the tool output as a message.
    """
    result = tool_node.invoke(state)

    # ToolNode returns {'messages': [message]} so we unwrap correctly
    tool_msg = result["messages"][0]

    return {"messages": state["messages"] + [tool_msg]}


# -----------------------------------------------------------
# Build the LangGraph conversational pipeline
# -----------------------------------------------------------
builder = StateGraph(ChatState)

builder.add_node("llm", llm_node)
builder.add_node("tools", tools_node)

# Conversation starts at LLM
builder.add_edge(START, "llm")

# After tools → go back to LLM
builder.add_edge("tools", "llm")

# After LLM → decide if tools or end
builder.add_conditional_edges(
    "llm",
    router,
    {"tools": "tools", "end": END}
)

graph = builder.compile()


# -----------------------------------------------------------
# CLI loop for interacting with the agent
# -----------------------------------------------------------
if __name__ == "__main__":
    state = {"messages": []}

    print('Type an instruction or "quit".\n')

    while True:
        user_message = input("> ")

        if user_message.lower() == "quit":
            break

        state["messages"].append(
            {"role": "user", "content": user_message}
        )

        # Run the graph once per message
        state = graph.invoke(state)

        # Print the latest model output
        print(state["messages"][-1].content, "\n")
