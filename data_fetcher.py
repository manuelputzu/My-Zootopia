import requests

API_KEY = 'R0ureXSm0jjtgBL5vVbpIg==V54rVqIItJYSAZT7'

def fetch_data(name):
    """
    Fetches the animal data.
    """
    api_url = f'https://api.api-ninjas.com/v1/animals?name={name}'
    headers = {
        'X-Api-Key': API_KEY
    }

    # Send GET request
    response = requests.get(api_url, headers=headers)

    # Check if request is successful
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Sorry there is a Failure: {response.status_code}")


def search_animal(animals_data, search_name):
    """Search for the animal"""
    found = False
    for animal in animals_data:
        if animal.get('name', '').lower() == search_name.lower():
            found = True
    return found