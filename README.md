# Zootopia

Zootopia is a simple Python project that generates an HTML page with animal information based on user input. It fetches data for a given animal name or type and formats it into visually appealing cards using basic CSS.

## Features

- Takes user input for an animal name or type (e.g., "Cheetah" or "Fox").

- Generates an HTML page dynamically with corresponding animal information.

- If a generic type (e.g., "Fox") is entered, multiple cards will be displayed for different types of that animal.

- Currently, the code searches for any animal that contains the input in its name (e.g., searching for "cat" will also display "catfish").

## Installation


Install dependencies:

pip install -r requirements.txt


## Usage

When prompted, enter the name or type of an animal.

The program will fetch relevant data and create an HTML file (animals.html).

Open animals.html in a browser to view the generated animal cards.