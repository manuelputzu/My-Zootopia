import requests


# Function to get animal data from the API
def get_animal_data(name, api_key):
    """ Fetch animal data from the API based on the animal's name. """
    api_url = f'https://api.api-ninjas.com/v1/animals?name={name}'

    # The headers with the API key
    headers = {
        'X-Api-Key': api_key
    }

    # Send GET request to the API
    response = requests.get(api_url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        return response.json()  # Return the parsed JSON data
    else:
        raise Exception(f"Failed to fetch data. HTTP Status code: {response.status_code}")


# Function to generate HTML content for each animal in the new format
def generate_animal_info(animals_data):
    output = ''
    for animal in animals_data:
        output += '<li class="cards__item">\n'

        # Add Name as a title
        if 'name' in animal:
            output += f"<div class='card__title'>{animal['name']}</div>\n"

        output += "<p class='card__text'>\n"

        # Add Location
        if 'locations' in animal and len(animal['locations']) > 0:
            output += f"<strong>Location:</strong> {animal['locations'][0]}<br/>\n"

        # Add Type
        if 'characteristics' in animal and 'type' in animal['characteristics']:
            output += f"<strong>Type:</strong> {animal['characteristics']['type']}<br/>\n"

        # Add Diet
        if 'characteristics' in animal and 'diet' in animal['characteristics']:
            output += f"<strong>Diet:</strong> {animal['characteristics']['diet']}<br/>\n"

        output += "</p>\n</li>\n"

    return output


# Function to write the updated HTML content
def write_html_file(template_path, output_html_path, animals_info):
    # Read the HTML template
    with open(template_path, 'r') as file: # Read the HTML template
        html_content = file.read()

    # Replace the placeholder with the generated animal information
    updated_html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", animals_info)

    # Write the updated HTML to a new file
    with open(output_html_path, 'w') as file:
        file.write(updated_html_content)


# Main function to run the script
def main():
    search_name = input("Please enter a name of an animal: ")  # The name of the animal you want to search for
    api_key = 'R0ureXSm0jjtgBL5vVbpIg==V54rVqIItJYSAZT7'  # API Key

    # Define the paths for the template and output
    template_path = 'animals_template.html'
    output_html_path = 'animals.html'

    try:
        # Fetch the animal data
        animals_data = get_animal_data(search_name, api_key)

        # Generate the animal info HTML
        animals_info_html = generate_animal_info(animals_data)

        # Write the updated HTML content to a new file
        write_html_file(template_path, output_html_path, animals_info_html)

        print(f"Successfully wrote animal data to {output_html_path}")

    except Exception as e:
        print(f"Error: {e}")


# Run the main function
if __name__ == "__main__":
    main()
