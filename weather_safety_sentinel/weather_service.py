import requests
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

def fetch_weather(city: str) -> dict:
    # URL for Algiers (Lat: 36.75, Lon: 3.04) as an example
    url = "https://api.open-meteo.com/v1/forecast?latitude=36.75&longitude=3.04&current=temperature_2m,wind_speed_10m"
    
    # Retrieve the token from the environment variable
    token: str | None = os.getenv("MOCK_TOKEN_123")
    if not token:
        return {"error": "Authentication token is missing. Please set the MOCK_TOKEN_123 environment variable."}
    
    headers = {"Authorization": f"Bearer {token}"}
    
    try:
        # Make the request
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        
        # Parse the JSON response
        data = response.json()
        return data
    
    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        return {"error": f"Network error occurred: {str(e)}"}
    
    except ValueError as e:
        # Handle JSON decoding errors
        return {"error": f"Failed to parse JSON response: {str(e)}"}