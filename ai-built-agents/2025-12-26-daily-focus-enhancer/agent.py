import os
import sys
from dotenv import load_dotenv
from langgraph import Graph
from openai import OpenAI
from schemas import FocusInput, FocusOutput
from graph import focus_graph


def main():
    load_dotenv()
    try:
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError('OPENAI_API_KEY not found in environment variables.')
        openai_client = OpenAI(api_key=api_key)
        
        # Get user input
        user_input = input('Enter your tasks and current focus challenges: ')
        
        # Validate input
        focus_input = FocusInput(user_input=user_input)
        
        # Run the focus enhancement process
        focus_output = focus_graph.run(focus_input)
        print(focus_output)
        
    except Exception as e:
        print(f'Error: {e}')
        sys.exit(1)


if __name__ == "__main__":
    main()
