import requests
import time
import json  # Import the json module


def fetch_all_earth_residents():
    url = "https://rickandmortyapi.com/api/character"
    earth_residents = []
    page_count = 0

    while url and page_count < 2:  # Limit to 5 pages to prevent infinite loops
        page_count += 1
        print(f"📡 Fetching Page {page_count}...")

        try:
            response = requests.get(
                headers={"Authorization": "Bearer MOCK_TOKEN_123"}, url=url, timeout=5
            )
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
            data = response.json()
            earth_residents.extend(data.get("results", []))
            # Save the list into a file as JSON
            with open("earth_residents.txt", "a", encoding="utf-8") as f:
                json.dump(earth_residents, f, ensure_ascii=False, indent=4)
                f.write("\n")
            # Empty the list to free up memory
            earth_residents.clear()
            url = data.get("info", {}).get("next")  # Get the next page URL
        except requests.exceptions.RequestException as e:
            print(f"Network error occurred: {str(e)}. Retrying in 5 seconds...")
            time.sleep(5)  # Wait before retrying
        except ValueError as e:
            print(f"Failed to parse JSON response: {str(e)}. Retrying in 5 seconds...")
            time.sleep(5)  # Wait before retrying
        # Catch file exceptions when writing to the file
        except IOError as e:
            print(f"File error occurred: {str(e)}. Retrying in 5 seconds...")
            time.sleep(5)  # Wait before retrying
        # Catch any other unexpected exceptions
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}. Retrying in 5 seconds...")
            time.sleep(5)  # Wait before retrying
        print(
            f"✅ Completed fetching all residents. Total residents: {len(earth_residents)}"
        )


if __name__ == "__main__":
    fetch_all_earth_residents()
