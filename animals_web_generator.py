import json


# Load data from the JSON file
def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


# Function to print the animal information
def print_animal_info(animals_data):
    for animal in animals_data:
        # Print Name
        if 'name' in animal:
            print(f"Name: {animal['name']}")

        # Print Diet
        if 'characteristics' in animal and 'diet' in animal['characteristics']:
            print(f"Diet: {animal['characteristics']['diet']}")

        # Print Location
        if 'locations' in animal and len(animal['locations']) > 0:
            print(f"Location: {animal['locations'][0]}")

        # Print Type
        if 'characteristics' in animal and 'type' in animal['characteristics']:
            print(f"Type: {animal['characteristics']['type']}")

        # Add a separator between animals
        print()  # Print a new line for better readability


# Load the data from animals_data.json
animals_data = load_data('/Users/manuelputzu/Documents/2024/Masterschool/PyCharm/Academy/SE104_intro_to_web/SE104_4_css/css_zootopia/animals_data.json')

# Print the animals' information
print_animal_info(animals_data)
