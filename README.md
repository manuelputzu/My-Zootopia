# Animal Data Fetcher and Website Generator

## Overview
Welcome to the Animal Data Fetcher and Website Generator! This project fetches cool animal data from an API and creates a nice HTML page to show off that information. We’ve split things into two parts: one for getting the data and another for generating the website. This keeps everything neat and tidy!

## Features
- Get animal data based on what you type in.
- Generate a simple HTML page to display the animal info.
- Uses environment variables to keep sensitive stuff, like API keys, safe and sound.

## Requirements
You’ll need Python 3 to run this project. Also, make sure you have these packages:
- `requests`
- `python-dotenv`

You can install all the required packages with this command:

```bash
pip install -r requirements.txt
```

## Setup
1. **Clone the Repo**:
   Grab a copy of this repository by running:
   ```bash
   git clone <your-repo-url>
   ```

2. **Create a `.env` File**:
   In the root of the project, make a new file called `.env` and put your API key in there:
   ```env
   API_KEY=your_actual_api_key_here
   ```

3. **Install the Packages**:
   Don't forget to install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To run the program, just type this in your terminal:
```bash
python animals_web_generator.py
```
You’ll be prompted to enter the name of an animal. The program will fetch the data and generate an HTML file called `animals.html`.

## File Structure
Here’s a quick look at how everything is organized:
```
/your-project
    ├── .env                   # This is where you keep sensitive info (not tracked by Git)
    ├── .gitignore              # Lists files Git should ignore
    ├── animals_template.html    # The HTML template we use
    ├── animals_web_generator.py  # This is the main script that creates the website
    ├── data_fetcher.py          # The module that fetches data from the API
    ├── requirements.txt         # Lists the required packages
    └── README.md                # This file contains information about the project
```

## Contributing
If you want to help out, feel free to fork the repo and send a pull request. I'd love to see your ideas!

## License
This project is under the MIT License, so feel free to use it as you like. Check out the LICENSE file for more details.
