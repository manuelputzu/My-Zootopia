import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Grab the API key from the environment
API_KEY = os.getenv('API_KEY')


def fetch_data(animal_name):
    """
    This function talks to the API and gets the animal data.
    It returns a list of animals, where each animal is a dictionary.
    """
    api_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    headers = {
        'X-Api-Key': API_KEY  # Using the API key from the .env file
    }

    # Send the request to the API
    response = requests.get(api_url, headers=headers)

    # Check if everything went okay (status code 200 means success)
    if response.status_code == 200:
        return response.json()  # If good, return the data in JSON form
    else:
        # If something went wrong, raise an error and show the status code
        raise Exception(f"Failed to fetch data. HTTP Status code: {response.status_code}")


def search_animal(animals_data, search_name):
    """Looks through the list to find a specific animal."""
    found = False  # Start by assuming it's not there

    for animal in animals_data:
        # If the name matches (case doesn't matter), mark as found
        if animal.get('name', '').lower() == search_name.lower():
            found = True

    return found  # Return True if we found it, False if not
