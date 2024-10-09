import requests


# Function to get animal data from the API
def get_animal_data(name):
    """ Fetch animal data from the API based on the animal's name. """
    api_url = f'https://api.api-ninjas.com/v1/animals?name={name}'

    # The headers with the API key
    headers = {
        'X-Api-Key': 'R0ureXSm0jjtgBL5vVbpIg==V54rVqIItJYSAZT7'
    }

    # Send GET request to the API
    response = requests.get(api_url, headers=headers)

    # Check if the request was successful
    if response.status_code == requests.codes.ok:
        return response.json()  # Return the parsed JSON data
    else:
        raise Exception(f"Failed to fetch data. HTTP Status code: {response.status_code}")


# Function to generate HTML content for each animal in the new format
def generate_animal_info(animals_data):
    output = ''
    for animal in animals_data:
        # Start creating the HTML block for each animal
        output += '<li class="cards__item">\n'

        # Add Name as a title
        if 'name' in animal:
            output += f"<div class='card__title'>{animal['name']}</div>\n"

        # Start the text section
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

        # Close the text section
        output += "</p>\n"

        # Close the HTML block for the animal
        output += '</li>\n'

    return output

# Function to write the updated HTML content
def write_html_file(template_path, output_html_path, animals_info):
    # Read the HTML template
    with open("animals_template.html", 'r') as file:
        html_content = file.read()

    # Replace the placeholder with the generated animal information
    updated_html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", animals_info)

    # Write the updated HTML to a new file
    with open("animals.html", 'w') as file:
        file.write(updated_html_content)

# Main function to run the script
def main():
    name = 'fox'  # The name of the animal you want to search for

    # Load the animal data
    animals_data = get_animal_data(name)

    # Generate the animal info HTML
    animals_info_html = generate_animal_info(animals_data)

    # Write the updated HTML content to a new file
    write_html_file('/Users/manuelputzu/Documents/2024/Masterschool/PyCharm/Academy/SE104_intro_to_web/SE104_4_css/css_zootopia/animals_template.html', '/Users/manuelputzu/Documents/2024/Masterschool/PyCharm/Academy/SE104_intro_to_web/SE104_4_css/css_zootopia/animals.html', animals_info_html)

# Run the main function
if __name__ == "__main__":
    main()
