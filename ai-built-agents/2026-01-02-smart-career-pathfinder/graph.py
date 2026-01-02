from langgraph import State, Transition, StateMachine
from prompts import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE
from schemas import CareerInput, CareerRecommendation
import openai


def fetch_job_market_data(skills, interests):
    # Placeholder function to simulate fetching job market data
    return ["Data Scientist", "Software Engineer", "Product Manager"]


def get_recommendations(input_data: CareerInput) -> CareerRecommendation:
    # Fetch job market data
    job_market_data = fetch_job_market_data(input_data.skills, input_data.interests)

    # Generate prompt for OpenAI
    user_prompt = USER_PROMPT_TEMPLATE.format(
        name=input_data.name,
        skills=", ".join(input_data.skills),
        interests=", ".join(input_data.interests),
        current_job=input_data.current_job or "None",
    )

    # Call OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=SYSTEM_PROMPT + user_prompt,
        max_tokens=150
    )

    # Extract recommendations
    recommendations = response.choices[0].text.strip().split("\n")

    return CareerRecommendation(
        recommended_careers=recommendations,
        rationale="Recommendations based on skills, interests, and current job market trends."
    )


# Define states
start_state = State(name="start", handler=get_recommendations)

# Define transitions
transitions = [
    Transition(source="start", target="end", condition=lambda x: True)
]

# Define state machine
career_state_machine = StateMachine(
    states=[start_state],
    transitions=transitions,
    initial_state="start"
)
