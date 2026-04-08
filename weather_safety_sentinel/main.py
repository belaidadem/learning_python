from weather_service import fetch_weather
from schema import WeatherReport
from pydantic import ValidationError

def main():
    # Example city
    city = "Algiers"
    
    # Fetch weather data
    print(f"Fetching weather data for {city}...")
    weather_data = fetch_weather(city)
    
    # Check for errors in the response
    if "error" in weather_data:
        print(weather_data["error"])
        return
    
    # Validate and parse the data using WeatherReport
    try:
        report = WeatherReport(**weather_data)
        print("Weather data successfully fetched and validated!")
        
        # Display the weather report
        print(f"Location: {report.latitude}, {report.longitude}")
        print(f"Timezone: {report.timezone} ({report.timezone_abbreviation})")
        print(f"Elevation: {report.elevation} meters")
        print(f"Temperature: {report.current.temperature_2m}°C")
        print(f"Wind Speed: {report.current.wind_speed_10m} km/h")
    
    except ValidationError as e:
        print("Failed to validate weather data:")
        print(e)

if __name__ == "__main__":
    main()