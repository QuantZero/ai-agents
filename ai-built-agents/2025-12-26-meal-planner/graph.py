# graph.py

from langgraph import State, Transition
from prompts import MEAL_PLANNER_PROMPT, USER_PROMPT_TEMPLATE
from langchain_openai import OpenAI
from schemas import MealPlanOutput


def meal_planner_graph():
    return [
        State(
            name="generate_meal_plan",
            action=generate_meal_plan,
            transitions=[Transition(condition=lambda output: True, target="output_result")]
        ),
        State(
            name="output_result",
            action=output_result,
            transitions=[]
        )
    ]


def generate_meal_plan(input_data):
    llm = OpenAI()
    user_prompt = USER_PROMPT_TEMPLATE.format(**input_data)
    response = llm.query(MEAL_PLANNER_PROMPT + user_prompt)
    # Parse response into structured output
    meals, shopping_list = parse_response(response)
    return MealPlanOutput(meals=meals, shopping_list=shopping_list)


def output_result(output_data):
    return output_data


def parse_response(response: str):
    # Dummy parser for response, replace this with actual parsing logic
    # Assuming response format: "Meal1, Meal2; Item1, Item2"
    meals, shopping_list = response.split(';')
    return meals.split(','), shopping_list.split(',')