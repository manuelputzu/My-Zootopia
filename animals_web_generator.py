import json
"""
Change the HTML using Python and the template replacement for the animals automatically.
"""

class AnimalDataProcessor:
    """Class responsible for processing animal data and generating HTML."""

    def __init__(self, data_path, template_path, output_html_path):
        """
        Initialize the AnimalDataProcessor with file paths.

        :param data_path: Path to the JSON file with animal data.
        :param template_path: Path to the HTML template file.
        :param output_html_path: Path to the output HTML file.
        """
        self.data_path = data_path
        self.template_path = template_path
        self.output_html_path = output_html_path
        self.animals_data = self.load_data()

    def load_data(self):
        """Load data from the JSON file."""
        with open(self.data_path, "r", encoding="utf-8") as handle:
            return json.load(handle)

    def generate_animal_info(self):
        """Generate HTML content for each animal."""
        output = ''
        for animal in self.animals_data:
            # Start creating the HTML block for each animal
            output += '<li class="cards__item">\n'

            # Add Name as a title
            if 'name' in animal:
                output += f"  <div class='card__title'>{animal['name']}</div>\n"

            output += "  <p class='card__text'>\n"

            # Add Location
            if 'locations' in animal and len(animal['locations']) > 0:
                output += f"    <strong>Location:</strong> {animal['locations'][0]}<br/>\n"

            # Add Type
            if 'characteristics' in animal and 'type' in animal['characteristics']:
                output += f"    <strong>Type:</strong> {animal['characteristics']['type']}<br/>\n"

            # Add Diet
            if 'characteristics' in animal and 'diet' in animal['characteristics']:
                output += f"    <strong>Diet:</strong> {animal['characteristics']['diet']}<br/>\n"

            output += "  </p>\n"
            output += '</li>\n'

        return output

    def write_html_file(self, animals_info):
        """
        Write the updated HTML content to a new file by replacing the placeholder with animal information.

        :param animals_info: The HTML content with animal data.
        """
        with open(self.template_path, 'r', encoding="utf-8") as file:
            html_content = file.read()

        # Replace the placeholder with the generated animal information
        updated_html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", animals_info)

        # Write the updated HTML to a new file
        with open(self.output_html_path, 'w', encoding="utf-8") as file:
            file.write(updated_html_content)

    def process(self):
        """Load data, generate HTML, and write the final output."""
        animals_info_html = self.generate_animal_info()
        self.write_html_file(animals_info_html)


def main():
    """Main function to run the animal data processing."""
    data_path = 'animals_data.json'
    template_path = 'animals_template.html'
    output_html_path = 'animals.html'

    processor = AnimalDataProcessor(data_path, template_path, output_html_path)
    processor.process()


if __name__ == "__main__":
    main()
