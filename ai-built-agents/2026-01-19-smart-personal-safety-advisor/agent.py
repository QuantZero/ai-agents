import os
import sys
import logging
from dotenv import load_dotenv
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from pydantic import BaseModel
import requests
from langchain_openai import OpenAI
from schemas import LocationInput, SafetyAdviceOutput
from graph import SafetyAdvisorStateMachine

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Environment variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

if not OPENAI_API_KEY:
    logger.error("OPENAI_API_KEY not set in the environment.")
    sys.exit(1)

# Initialize OpenAI client
openai_client = OpenAI(api_key=OPENAI_API_KEY)

# Initialize Geolocator
geolocator = Nominatim(user_agent="smart_personal_safety_advisor")


def get_location_coordinates(location_name: str):
    try:
        location = geolocator.geocode(location_name)
        if location:
            return location.latitude, location.longitude
        else:
            raise ValueError("Could not find location.")
    except GeocoderTimedOut as e:
        logger.error("Geocoding service timed out.", exc_info=e)
        raise


def get_safety_advice(location_input: LocationInput) -> SafetyAdviceOutput:
    latitude, longitude = get_location_coordinates(location_input.location_name)
    # Placeholder for real-time safety data retrieval
    safety_data = retrieve_safety_data(latitude, longitude)
    # Construct prompt for AI
    prompt = (f"You are a safety advisor AI. Provide safety advice for latitude: {latitude}, "
              f"longitude: {longitude}. Current conditions: {safety_data}")
    advice = openai_client.complete(prompt)
    return SafetyAdviceOutput(advice=advice)


def retrieve_safety_data(latitude: float, longitude: float) -> str:
    # Placeholder implementation for retrieving safety data
    # This could be replaced with real APIs that provide safety information
    logger.info(f"Retrieving safety data for coordinates: ({latitude}, {longitude})")
    return "Clear skies, moderate traffic, low crime rate."


def main():
    try:
        location_name = input("Enter the location you want safety advice for: ")
        location_input = LocationInput(location_name=location_name)
        safety_advice = get_safety_advice(location_input)
        print(f"Safety Advice: {safety_advice.advice}")
    except Exception as e:
        logger.error("An error occurred during execution.", exc_info=e)


if __name__ == "__main__":
    main()