import os
import sys
from dotenv import load_dotenv
from typing import Any
from schemas import UserPreferences, EnergyRecommendations
from graph import EnergyFlow
from tools import fetch_user_data, log_recommendations

load_dotenv()

class SmartDailyEnergyManager:
    def __init__(self):
        self.flow = EnergyFlow()
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not set in environment variables.")

    def get_recommendations(self, user_prefs: UserPreferences) -> EnergyRecommendations:
        try:
            user_data = fetch_user_data(user_prefs.user_id)
            recommendations = self.flow.run(user_data)
            log_recommendations(user_prefs.user_id, recommendations)
            return recommendations
        except Exception as e:
            print(f"Error during recommendation generation: {e}", file=sys.stderr)
            sys.exit(1)

if __name__ == "__main__":
    # Example CLI interface
    if len(sys.argv) != 3:
        print("Usage: python agent.py <user_id> <wake_time>")
        sys.exit(1)
    user_id = sys.argv[1]
    wake_time = sys.argv[2]
    user_prefs = UserPreferences(user_id=user_id, wake_time=wake_time)
    manager = SmartDailyEnergyManager()
    recommendations = manager.get_recommendations(user_prefs)
    print("Recommendations:", recommendations)
