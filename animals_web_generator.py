import data_fetcher

# Function to generate HTML content for each animal in the new format
def generate_animal_info(animals_data):
    """Builds HTML for animal data."""
    output = ''
    for animal in animals_data:
        output += '<li class="cards__item">\n'

        if 'name' in animal:
            output += f"<div class='card__title'>{animal['name']}</div>\n"

        output += "<p class='card__text'>\n"

        if 'locations' in animal and len(animal['locations']) > 0:
            output += f"<strong>Location:</strong> {animal['locations'][0]}<br/>\n"

        if 'characteristics' in animal and 'type' in animal['characteristics']:
            output += f"<strong>Type:</strong> {animal['characteristics']['type']}<br/>\n"

        if 'characteristics' in animal and 'diet' in animal['characteristics']:
            output += f"<strong>Diet:</strong> {animal['characteristics']['diet']}<br/>\n"

        output += "</p>\n</li>\n"

    return output


# Function to write the updated HTML content
def write_html_file(template_file, output_file, animals_info):
    """
    Reads the HTML template, replaces placeholder with the
    animal info, and writes it to a new HTML file.
    """
    with open(template_file, 'r') as file:  # open the template file
        html_content = file.read()

    # Replace the placeholder in the template with the animal info
    updated_html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", animals_info)

    # Write the updated content to the output file
    with open(output_file, 'w') as file:
        file.write(updated_html_content)


# Main function to run the script
def main():
    # Prompt user for an animal name
    animal_name = input("Please enter an animal: ")

    # Define the template and output files
    template_file = 'animals_template.html'  # The HTML template file
    output_file = 'animals.html'  # Where to save the generated HTML

    try:
        # Fetch the animal data
        animals_data = data_fetcher.fetch_data(animal_name)

        # Check if the animal exists in the data
        if data_fetcher.search_animal(animals_data, animal_name):
            # Generate the animal info HTML
            animals_info_html = generate_animal_info(animals_data)
        else:
            # If animal doesn't exist, show an error message in HTML
            animals_info_html = f"<h2>You entered: '{animal_name}'.\nThat animal doesn't exist in our database.</h2>\n"

        # Write the updated HTML content to the output file
        write_html_file(template_file, output_file, animals_info_html)

        print(f"Successfully wrote animal data to {output_file}")

    except Exception as e:
        # Print any errors that occurred
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
