import json

def load_data(filepath):
    """simple func to load json data from local dir"""
    with open(filepath, "r") as handle:
        return json.load(handle)


def get_info_for_each_animal(animals_data):
    """get the info for each animal and return it"""
    output =''
    for animal in animals_data:
        output += serialize_animal(animal)
    return output


def serialize_animal(animal):
    """Sterilizing the data into HTML conform text"""
    output = ''
    output += '<li class="cards__item">'
    output += f'<div class="card__title">{animal['name']}</div><br/>'
    output += '<div class="card__text">'
    output += '<ul>'
    output += f'<li><strong>Diet:</strong> {animal['taxonomy']['order']}</li>'
    output += f'<li><strong>Location:</strong> {animal['locations'][0]}</li>'
    try:
        output += f'<li><strong>Type:</strong> {animal['characteristics']['type']}</li>'
        output += '</ul></div></li>'
    except KeyError:
        output += '</ul></div></li>'
    return output


def content_temp(html):
    """reading the template and return it as a string"""
    HTMLFile = open(html, 'r')
    index = HTMLFile.read()
    return index


def write_new_html(new_code):
    """Creating a new html file"""
    new = open('animals.html', 'w')
    new.write(new_code)
    new.close()


def main():
    """get the data needed and convert it into a new HTML file"""
    animals_data = load_data('animals_data.json')
    content = get_info_for_each_animal(animals_data)
    code = content_temp('animals_template.html')
    new_code = code.replace('__REPLACE_ANIMALS_INFO__', content)
    write_new_html(new_code)


if __name__ == "__main__":
    main()
