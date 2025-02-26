import json
from bs4 import BeautifulSoup
import requests

def load_data(filepath):
    with open(filepath, "r") as handle:
        return json.load(handle)


def get_info_for_each_animal(animals_data):
    output = ''
    for animal in animals_data:
        output += '<li class="cards__item">'
        output += f'<div class="card__title">{animal['name']}</div><br/>'
        output += f'<strong>Diet:</strong> {animal['taxonomy']['order']}<br/><br/>'
        output += f'<strong>Location:</strong> {animal['locations'][0]}<br/><br/>'
        try:
            output += f'<strong>Type:</strong> {animal['characteristics']['type']}<br/><br/>'
            output += '</li>'
        except KeyError:
            output += '</li>'
            continue
    return output



def content_temp(html):
    HTMLFile = open(html, 'r')
    index = HTMLFile.read()
    return index

def write_new_html(new_code):
    new = open('animals.html', 'w')
    new.write(new_code)
    new.close()


def main():
    animals_data = load_data('animals_data.json')
    content = get_info_for_each_animal(animals_data)
    code = content_temp('animals_template.html')
    new_code = code.replace('__REPLACE_ANIMALS_INFO__', content)
    write_new_html(new_code)



if __name__ == "__main__":
    main()
