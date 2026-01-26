from openai import OpenAIManager

openai_manager = OpenAIManager()

def get_energy_optimization_recommendations(system_prompt: str, user_prompt: str):
    response = openai_manager.generate_response(system_prompt, user_prompt)
    return response
