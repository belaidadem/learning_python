from enum import Enum, auto
from pydantic import BaseModel, Field


class SafetyLevel(str, Enum):
    # TODO: Define SAFE, WARNING, DANGER
    def __generate_next_value_(name, start, count, last_values) -> str:
        return name.lower()

    SAFE: str = auto()
    WARNING: str = auto()
    DANGER: str = auto()


class WeatherReport(BaseModel):
    # Define the fields with descriptions
    city: str = Field(description="The name of the city.")
    latitude: float = Field(description="The latitude of the location.")
    longitude: float = Field(description="The longitude of the location.")
    # generation_time_ms: float = Field(description="The time taken to generate the weather data, in milliseconds.")
    utc_offset_seconds: int = Field(description="The UTC offset in seconds.")
    timezone: str = Field(description="The timezone of the location.")
    timezone_abbreviation: str = Field(description="The abbreviation of the timezone.")
    elevation: float = Field(description="The elevation of the location in meters.")

    class CurrentUnits(BaseModel):
        time: str = Field(description="The format of the time (e.g., iso8601).")
        interval: str = Field(description="The interval unit for time.")
        temperature_2m: str = Field(description="The unit for temperature at 2 meters.")
        wind_speed_10m: str = Field(description="The unit for wind speed at 10 meters.")

    current_units: CurrentUnits = Field(
        description="The units for the current weather data."
    )

    class Current(BaseModel):
        time: str = Field(description="The timestamp of the current weather data.")
        interval: int = Field(
            description="The interval in seconds for the current weather data."
        )
        temperature_2m: float = Field(
            description="The current temperature at 2 meters in Celsius."
        )
        wind_speed_10m: float = Field(
            description="The current wind speed at 10 meters in km/h."
        )

    current: Current = Field(description="The current weather data.")
