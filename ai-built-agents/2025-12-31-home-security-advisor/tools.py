# tools.py

import requests
import logging

logger = logging.getLogger(__name__)


def get_crime_data(address: str) -> dict:
    """
    Fetches crime data for the given address using a hypothetical crime data API.
    """
    # Hypothetical API endpoint
    api_url = f"https://api.crime-data.com/crimes?address={address}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logger.error(f"Error fetching crime data: {e}")
        return {}


def evaluate_security(crime_data: dict) -> str:
    """
    Evaluates the security of a location based on crime data and provides recommendations.
    """
    # Simple evaluation logic based on crime data
    if not crime_data or 'crime_score' not in crime_data:
        return "Unable to fetch crime data."
    crime_score = crime_data.get('crime_score', 0)
    if crime_score > 75:
        return "High crime area. Consider upgrading your security systems and installing surveillance cameras."
    elif 50 < crime_score <= 75:
        return "Moderate crime area. Ensure all entry points are secured and consider a security system."
    else:
        return "Low crime area. Basic security measures should suffice."
