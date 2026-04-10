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
