import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Import the functions from main.py
from main import (
    generate_clarifying_questions,
    generate_requirements_spec,
    generate_builder_prompt,
)

load_dotenv(override=True)

# Page configuration
st.set_page_config(
    page_title="MVP Planner Agent",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS for dark theme styling
st.markdown("""
    <style>
    /* Dark theme base */
    [data-testid="stAppViewContainer"] {
        background-color: #0e1117;
    }
    .main {
        background-color: #0e1117;
    }
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #64b5f6;
        text-align: center;
        margin-bottom: 2rem;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        color: #ffffff;
        line-height: 1.6;
    }
    .user-message {
        background-color: #1e3a5f;
        border-left: 4px solid #64b5f6;
        color: #ffffff;
    }
    .assistant-message {
        background-color: #1e3a52;
        border-left: 4px solid #81c784;
        color: #ffffff;
        margin-bottom: 0;
        border-radius: 0.5rem 0.5rem 0 0;
    }
    .assistant-wrapper {
        background-color: #1e3a52;
        border-left: 4px solid #81c784;
        border-radius: 0.5rem;
        padding: 1rem;
        margin-bottom: 1rem;
    }
    /* Ensure markdown content has white text */
    .assistant-wrapper p,
    .assistant-wrapper li,
    .assistant-wrapper ol,
    .assistant-wrapper ul,
    .assistant-wrapper div {
        color: #ffffff !important;
    }
    .assistant-wrapper .stMarkdown {
        color: #ffffff !important;
    }
    .assistant-wrapper .stMarkdown p,
    .assistant-wrapper .stMarkdown li,
    .assistant-wrapper .stMarkdown ol,
    .assistant-wrapper .stMarkdown ul {
        color: #ffffff !important;
    }
    /* Ensure text is readable in message boxes */
    .chat-message strong {
        color: #ffffff;
        font-weight: 600;
    }
    .chat-message p, .chat-message div, .chat-message span {
        color: #ffffff !important;
    }
    /* Dark theme for all markdown */
    .stMarkdown {
        color: #ffffff !important;
    }
    .stMarkdown p, .stMarkdown li, .stMarkdown ol, .stMarkdown ul {
        color: #ffffff !important;
    }
    /* Dark theme for text inputs */
    .stTextArea>div>div>textarea, .stTextInput>div>div>input {
        color: #ffffff !important;
        background-color: #1e1e1e !important;
    }
    /* Dark theme for select boxes */
    .stSelectbox>div>div {
        background-color: #1e1e1e !important;
        color: #ffffff !important;
    }
    /* Button styling */
    .stButton>button {
        width: 100%;
        background-color: #4caf50;
        color: white;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    /* Sidebar dark theme */
    [data-testid="stSidebar"] {
        background-color: #1e1e1e;
    }
    [data-testid="stSidebar"] .stMarkdown {
        color: #ffffff !important;
    }
    /* Info boxes dark theme */
    .stInfo {
        background-color: #1e3a5f;
        color: #ffffff;
    }
    .stSuccess {
        background-color: #1e3a52;
        color: #ffffff;
    }
    .stWarning {
        background-color: #3d2e1e;
        color: #ffffff;
    }
    .stError {
        background-color: #3d1e1e;
        color: #ffffff;
    }
    /* Subheader and headers */
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
    }
    /* Expander dark theme */
    .streamlit-expanderHeader {
        background-color: #1e1e1e;
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "step" not in st.session_state:
    st.session_state.step = "idea"
    st.session_state.idea = ""
    st.session_state.questions = ""
    st.session_state.answers = ""
    st.session_state.requirements_spec = ""
    st.session_state.builder_prompt = ""
    st.session_state.chat_history = []


def reset_session():
    """Reset the session to start over"""
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.session_state.step = "idea"
    st.session_state.idea = ""
    st.session_state.questions = ""
    st.session_state.answers = ""
    st.session_state.requirements_spec = ""
    st.session_state.builder_prompt = ""
    st.session_state.chat_history = []


def add_to_chat(role: str, content: str):
    """Add a message to chat history"""
    st.session_state.chat_history.append({"role": role, "content": content})


def main():
    # Header
    st.markdown('<div class="main-header">🚀 MVP Planner Agent</div>', unsafe_allow_html=True)
    st.markdown("---")

    # Sidebar for controls
    with st.sidebar:
        st.header("Controls")
        if st.button("🔄 Start Over", use_container_width=True):
            reset_session()
            st.rerun()
        
        st.markdown("---")
        st.markdown("### Progress")
        steps = {
            "idea": "1️⃣ Idea",
            "questions": "2️⃣ Questions",
            "answers": "3️⃣ Answers",
            "spec": "4️⃣ Spec",
            "prompt": "5️⃣ Builder Prompt"
        }
        current_step_idx = list(steps.keys()).index(st.session_state.step) + 1
        for i, (key, label) in enumerate(steps.items(), 1):
            if i < current_step_idx:
                st.markdown(f"✅ {label}")
            elif i == current_step_idx:
                st.markdown(f"🔄 {label}")
            else:
                st.markdown(f"⏳ {label}")

    # Main content area
    col1, col2 = st.columns([2, 1])

    with col1:
        # Chat history display
        st.subheader("💬 Conversation")
        
        # Display chat history
        for msg in st.session_state.chat_history:
            if msg["role"] == "user":
                # Escape HTML and preserve line breaks
                content = msg["content"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\n", "<br>")
                st.markdown(f'<div class="chat-message user-message"><strong style="color: #64b5f6; display: block; margin-bottom: 0.5rem;">You:</strong><div style="color: #ffffff;">{content}</div></div>', unsafe_allow_html=True)
            else:
                # For assistant messages, create a styled wrapper
                st.markdown(f'<div class="assistant-wrapper">', unsafe_allow_html=True)
                st.markdown(f'<div class="chat-message assistant-message"><strong style="color: #81c784; display: block; margin-bottom: 0.5rem;">Assistant:</strong></div>', unsafe_allow_html=True)
                # Render markdown content
                st.markdown(msg["content"])
                st.markdown('</div>', unsafe_allow_html=True)

        # Step 1: Get the idea
        if st.session_state.step == "idea":
            st.info("👋 Welcome! Let's start by describing your mobile app idea.")
            idea_input = st.text_area(
                "Briefly describe your mobile app idea:",
                value=st.session_state.idea,
                height=150,
                placeholder="e.g., A social fitness app that connects runners in local communities..."
            )
            
            if st.button("Submit Idea", type="primary"):
                if idea_input.strip():
                    st.session_state.idea = idea_input.strip()
                    add_to_chat("user", f"Idea: {st.session_state.idea}")
                    
                    with st.spinner("🤔 Generating clarifying questions..."):
                        try:
                            st.session_state.questions = generate_clarifying_questions(st.session_state.idea)
                            add_to_chat("assistant", f"Here are some clarifying questions:\n\n{st.session_state.questions}")
                            st.session_state.step = "questions"
                            st.rerun()
                        except Exception as e:
                            st.error(f"Error generating questions: {e}")
                else:
                    st.warning("Please enter an idea before submitting.")

        # Step 2: Show questions and get answers
        elif st.session_state.step == "questions":
            st.success("✅ Questions generated! Please answer them below.")
            
            # Display questions
            st.markdown("### 📋 Clarifying Questions")
            st.markdown(st.session_state.questions)
            
            st.markdown("---")
            answers_input = st.text_area(
                "Your answers (answer all questions in one block of text):",
                value=st.session_state.answers,
                height=300,
                placeholder="1. Target users are fitness enthusiasts aged 25-45...\n2. Primary use case is..."
            )
            
            col_btn1, col_btn2 = st.columns([1, 1])
            with col_btn1:
                if st.button("Submit Answers", type="primary"):
                    if answers_input.strip():
                        st.session_state.answers = answers_input.strip()
                        add_to_chat("user", f"Answers:\n\n{st.session_state.answers}")
                        
                        with st.spinner("📝 Generating requirements spec..."):
                            try:
                                st.session_state.requirements_spec = generate_requirements_spec(
                                    st.session_state.idea,
                                    st.session_state.answers
                                )
                                add_to_chat("assistant", f"Requirements Spec:\n\n{st.session_state.requirements_spec}")
                                st.session_state.step = "spec"
                                st.rerun()
                            except Exception as e:
                                st.error(f"Error generating spec: {e}")
                    else:
                        st.warning("Please provide answers before submitting.")
            
            with col_btn2:
                if st.button("← Back to Idea"):
                    st.session_state.step = "idea"
                    st.rerun()

        # Step 3: Show spec and confirm
        elif st.session_state.step == "spec":
            st.success("✅ Requirements spec generated!")
            
            st.markdown("### 📄 MVP & Technical Requirements Spec")
            st.markdown(st.session_state.requirements_spec)
            
            st.markdown("---")
            col_btn3, col_btn4 = st.columns([1, 1])
            
            with col_btn3:
                if st.button("Generate Builder Prompt", type="primary"):
                    with st.spinner("🔨 Generating builder prompt..."):
                        try:
                            st.session_state.builder_prompt = generate_builder_prompt(
                                st.session_state.requirements_spec
                            )
                            add_to_chat("assistant", f"Builder Prompt:\n\n{st.session_state.builder_prompt}")
                            st.session_state.step = "prompt"
                            st.rerun()
                        except Exception as e:
                            st.error(f"Error generating builder prompt: {e}")
            
            with col_btn4:
                if st.button("← Back to Answers"):
                    st.session_state.step = "questions"
                    st.rerun()

        # Step 4: Show final builder prompt
        elif st.session_state.step == "prompt":
            st.success("🎉 Builder prompt generated!")
            
            st.markdown("### 🚀 Builder Agent Prompt")
            st.text_area(
                "Builder Prompt (you can copy this):",
                value=st.session_state.builder_prompt,
                height=400,
                key="prompt_display"
            )
            
            # Download button
            st.download_button(
                label="📥 Download Builder Prompt",
                data=st.session_state.builder_prompt,
                file_name="builder_prompt.txt",
                mime="text/plain",
                type="primary"
            )
            
            if st.button("← Back to Spec"):
                st.session_state.step = "spec"
                st.rerun()

    with col2:
        st.subheader("📊 Current Output")
        
        if st.session_state.step == "idea":
            st.info("Enter your app idea to begin.")
        elif st.session_state.step == "questions":
            st.markdown("### Questions")
            st.markdown(st.session_state.questions)
        elif st.session_state.step == "spec":
            st.markdown("### Requirements Spec")
            with st.expander("View Spec", expanded=True):
                st.markdown(st.session_state.requirements_spec)
        elif st.session_state.step == "prompt":
            st.markdown("### Builder Prompt")
            with st.expander("View Prompt", expanded=True):
                st.text(st.session_state.builder_prompt[:500] + "..." if len(st.session_state.builder_prompt) > 500 else st.session_state.builder_prompt)


if __name__ == "__main__":
    # Check for API key
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    if not OPENAI_API_KEY:
        st.error("⚠️ OPENAI_API_KEY is not set. Please add it to a .env file in the mvp-planner-agent directory.")
        st.stop()
    
    main()

