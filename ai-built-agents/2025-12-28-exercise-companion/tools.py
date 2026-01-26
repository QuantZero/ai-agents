# tools.py

from openai import OpenAI


def generate_plan(state):
    """Generates a personalized exercise plan based on the user's input."""
    client = OpenAI()
    response = client.complete(prompt="Create a personalized exercise plan.", temperature=0.7)
    return {"personalized_plan": response['choices'][0]['text']}


def provide_motivation(state):
    """Provides motivational tips to keep the user engaged."""
    client = OpenAI()
    response = client.complete(prompt="Provide motivational tips.", temperature=0.7)
    return {"motivation_tips": response['choices'][0]['text']}
