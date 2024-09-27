import json


# Load data from the JSON file
def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


# Function to generate HTML content for each animal
def generate_animal_info(animals_data):
    output = ''
    for animal in animals_data:
        # Start creating the HTML block for each animal
        output += "<li class='cards__item'>\n"

        # Add Name
        if 'name' in animal:
            output += f"<div class='card__title'>Name: {animal['name']}</div>\n"

        # Add Diet
        if 'characteristics' in animal and 'diet' in animal['characteristics']:
            output += f"<div class='card__text'>Diet: {animal['characteristics']['diet']}</div>\n"

        # Add Location
        if 'locations' in animal and len(animal['locations']) > 0:
            output += f"<div class='card__text'>Location: {animal['locations'][0]}</div>\n"

        # Add Type
        if 'characteristics' in animal and 'type' in animal['characteristics']:
            output += f"<div class='card__text'>Type: {animal['characteristics']['type']}</div>\n"

        # Close the HTML block for the animal
        output += "</li>\n"

    return output


# Function to write the updated HTML content
def write_html_file(template_path, output_html_path, animals_info):
    # Read the HTML template
    with open(template_path, 'r') as file:
        html_content = file.read()

    # Replace the placeholder with the generated animal information
    updated_html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", animals_info)

    # Write the updated HTML to a new file
    with open(output_html_path, 'w') as file:
        file.write(updated_html_content)


# Main function to run the script
def main():
    # Load the animal data
    animals_data = load_data('animals_data.json')

    # Generate the animal info HTML
    animals_info_html = generate_animal_info(animals_data)

    # Write the updated HTML content to a new file
    write_html_file('animals_template.html', 'animals.html', animals_info_html)


# Run the main function
if __name__ == "__main__":
    main()
