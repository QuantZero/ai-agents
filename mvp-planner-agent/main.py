import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


load_dotenv(override=True)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

if not OPENAI_API_KEY:
    raise RuntimeError(
        "OPENAI_API_KEY is not set. Add it to a .env file in mvp-mobile-agent/."
    )


llm = ChatOpenAI(model=OPENAI_MODEL, temperature=0.2)


def generate_clarifying_questions(idea_summary: str) -> str:
    """
    Ask focused questions to nail down product + technical context
    for a modern mobile app MVP.
    """
    prompt = f"""
You are an expert mobile product+tech planner.

The user gave this high-level mobile app idea:
\"\"\"{idea_summary}\"\"\"

Ask 8–12 short, numbered questions (1., 2., 3., …) to clarify:
- target users and their concrete pain points
- primary use cases & key scenarios
- absolute must-have MVP features vs nice-to-have
- platforms & form factors (iOS, Android, web, tablet, watch, etc.)
- technical preferences (e.g., SwiftUI, Kotlin/Compose, React Native, Flutter, backend choices)
- data, privacy, and compliance concerns
- success metrics / business goals
- any constraints (budget, team size, delivery timeline)

Questions should be:
- concise and non-overlapping
- specific to this idea (avoid generic “tell me more”)
- phrased so a non-technical founder can answer them in plain language

Only output the questions, numbered on separate lines.
"""
    return llm.invoke(prompt).content  # type: ignore[return-value]


def generate_requirements_spec(idea_summary: str, answers: str) -> str:
    """
    Turn the idea + answers into a structured MVP+technical spec,
    grounded in modern mobile development practices.
    """
    prompt = f"""
You are a senior mobile architect and product lead.

High-level idea:
\"\"\"{idea_summary}\"\"\"

User's answers to clarification questions:
\"\"\"{answers}\"\"\"

Based on this, create a concise but detailed **MVP and technical requirements spec**
for a modern mobile app. Use markdown-style headings and bullet points.

Include sections:

1. Problem & Target Users
   - Who this is for and what concrete pain it solves.

2. Core Value Proposition
   - 2–3 sentences on why this app should exist.

3. Primary User Journeys
   - 3–6 key flows written as step-by-step bullets.

4. MVP Feature Set
   - Must-have features (MVP v1).
   - Nice-to-have features (later iterations).

5. Platforms, Devices & Accessibility
   - Target OSes (iOS, Android, web, etc.).
   - Any form-factor notes (phone, tablet, watch).
   - High-level accessibility expectations.

6. High-Level Technical Direction
   - Recommended client tech options:
     - e.g. SwiftUI, Kotlin/Compose, React Native, Flutter, Expo, etc.
   - Backend / data layer options:
     - e.g. Firebase, Supabase, custom API, serverless, local-only.
   - Storage, auth, analytics, and notifications at a high level.

7. Data Model & Integrations (High Level)
   - Main domain entities and relationships.
   - External APIs or SDKs (if any).

8. Constraints & Assumptions
   - Time/budget/team constraints.
   - Non-goals for MVP (what is explicitly out of scope).

9. Success Metrics
   - 3–6 measurable KPIs (activation, retention, engagement, revenue, etc.).

Keep it concrete and opinionated enough that a builder agent can design a real architecture,
but do NOT drift into implementation details or code.
"""
    return llm.invoke(prompt).content  # type: ignore[return-value]


def generate_builder_prompt(requirements_spec: str) -> str:
    """
    Turn the spec into a single, self-contained prompt for a separate "builder" agent.
    """
    prompt = f"""
You are an AI prompt engineer.

Your task is to write **one single, self-contained prompt** that will be given to
an AI-powered *MVP Builder Agent*.

That builder agent will:
- know modern mobile and backend stacks (SwiftUI, Kotlin/Compose, React Native/Expo, Flutter,
  Node/Express, Django/FastAPI, Firebase/Supabase, serverless, CI/CD, etc.),
- be capable of producing architecture plans and code-level scaffolding,
- follow best practices for clean code, modular design, and testability.

You are given the following validated MVP + technical requirements spec:

\"\"\"SPEC_START
{requirements_spec}
SPEC_END\"\"\"

Write a prompt that:
- Starts by clearly defining the **role** and mindset of the builder agent.
- Includes the full spec (between SPEC_START / SPEC_END) as context.
- Asks the builder to:
  - Propose a concrete tech stack choice (and justify briefly),
  - Design the architecture (layers, modules, data flow),
  - Define screens and navigation,
  - Define data models and API contracts,
  - Outline milestones / implementation phases,
  - (Optionally) suggest where to add tests, analytics, and monitoring.
- Uses clear bullet points and headings where appropriate.
- Uses explicit instructions about output format so it’s easy to consume in a dev workflow
  (e.g., “start with a short summary, then sections for stack, architecture, screens, data, APIs,
  milestones, risks”).

IMPORTANT:
- Your output must be **only the final prompt text** for the builder agent.
- Do NOT add any explanations or commentary outside of that prompt.
"""
    # The model returns the builder prompt as plain text; we just pass it through.
    return llm.invoke(prompt).content  # type: ignore[return-value]


def main() -> None:
    print("\n=== Mobile MVP Planner (Prompt-First) ===")
    print("This agent will help you refine an app idea and output a single builder prompt.\n")

    idea = input("Briefly describe your mobile app idea: ").strip()
    if not idea:
        print("No idea provided. Exiting.")
        return

    questions = generate_clarifying_questions(idea)
    print("\n=== CLARIFYING QUESTIONS ===\n")
    print(questions)
    print(
        "\nAnswer all of the questions above in ONE block of text.\n"
        "Tip: To avoid terminal limits, you can type '@path/to/file.txt' instead of answering here,\n"
        "and the planner will read your answers from that file.\n"
    )

    raw_input_str = input("Your answers (or @path/to/file): ").strip()

    # Allow answering via an external file so you can use your editor.
    if raw_input_str.startswith("@"):
        answers_path = raw_input_str[1:].strip()
        try:
            with open(answers_path, "r", encoding="utf-8") as f:
                answers = f.read().strip()
        except OSError as e:
            print(f"\nFailed to read answers file '{answers_path}': {e}")
            return
    else:
        answers = raw_input_str

    # Light guardrail: warn if the answer is extremely short.
    if len(answers) < 200:
        print(
            "\nNote: Your answers are quite short. The planner will still continue, "
            "but the spec (and builder prompt) may be generic.\n"
        )

    requirements_spec = generate_requirements_spec(idea, answers)

    print("\n=== PREVIEW: MVP & TECHNICAL SPEC ===\n")
    print(requirements_spec)

    confirm = input(
        "\nUse this spec to generate the final builder prompt? [y/N]: "
    ).strip().lower()
    if confirm != "y":
        print(
            "\nAborting prompt generation. Rerun the planner when you're ready with clearer answers."
        )
        return

    builder_prompt = generate_builder_prompt(requirements_spec)

    # Save full prompt to a file so it's easy to open and copy from your editor.
    output_path = "builder_prompt.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(builder_prompt)

    print("\n=== BUILDER AGENT PROMPT (PREVIEW) ===\n")
    # Show a short preview so the terminal isn't flooded.
    preview_lines = builder_prompt.splitlines()[:40]
    print("\n".join(preview_lines))

    print(
        f"\n[Saved full builder prompt to: {output_path}]\n"
        "Open that file in your editor to view and copy the complete prompt."
    )


if __name__ == "__main__":
    main()


