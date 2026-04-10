import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()


def get_db_connection():
    """Establishes a connection to the PostgreSQL database using credentials from environment variables."""
    try:
        conn = psycopg2.connect(os.getenv("NEON_POSTGRESQL_URL"))
        # print("Database connection established successfully.") # Uncomment for debugging
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        raise


def init_db():
    """Initializes the database by creating necessary tables."""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS weather_reports (
                id SERIAL PRIMARY KEY,
                city VARCHAR(255) NOT NULL,
                latitude FLOAT NOT NULL,
                longitude FLOAT NOT NULL,
                timezone VARCHAR(255) NOT NULL,
                timezone_abbreviation VARCHAR(10) NOT NULL,
                elevation FLOAT NOT NULL,
                temperature_2m FLOAT NOT NULL,
                wind_speed_10m FLOAT NOT NULL,
                report_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """
        )
        conn.commit()
        # print("Database initialized successfully.") # Uncomment for debugging
    except psycopg2.Error as e:
        print(f"Error initializing the database: {e}")
        raise
    finally:
        cursor.close()
        conn.close()


def save_weather_report(report):
    """Saves a weather report to the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO weather_reports (city, latitude, longitude, timezone, timezone_abbreviation, elevation, temperature_2m, wind_speed_10m)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """,
            (
                report.city,
                report.latitude,
                report.longitude,
                report.timezone,
                report.timezone_abbreviation,
                report.elevation,
                report.current.temperature_2m,
                report.current.wind_speed_10m,
            ),
        )
        conn.commit()
        # print("Weather report saved successfully.") # Uncomment for debugging
    except psycopg2.Error as e:
        print(f"Error saving weather report: {e}")
        raise
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    init_db()  # Initialize the database when the module is run directly
