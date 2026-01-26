# graph.py

from langgraph import Flow, Node
from prompts import SYSTEM_PROMPT, USER_PROMPT
from tools import generate_plan, provide_motivation


exercise_flow = Flow([
    Node(
        name="Start",
        prompt=SYSTEM_PROMPT,
        transitions={
            "GeneratePlan": lambda state: True
        }
    ),
    Node(
        name="GeneratePlan",
        tool=generate_plan,
        prompt=USER_PROMPT,
        transitions={
            "ProvideMotivation": lambda state: True
        }
    ),
    Node(
        name="ProvideMotivation",
        tool=provide_motivation,
        transitions={
            "End": lambda state: True
        }
    ),
    Node(
        name="End",
        prompt="Thank you for using the Exercise Companion!",
    )
])
