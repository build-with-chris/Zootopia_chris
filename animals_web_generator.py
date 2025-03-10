from data_fetcher import fetch_data


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
    output += f'<div class="card__title">{animal["name"]}</div><br/>'
    output += '<div class="card__text">'
    output += '<ul>'
    try:
        output += f'<li><strong>Diet:</strong> {animal["taxonomy"]["order"]}</li>'
    except KeyError:
        pass
    try:
        output += f'<li><strong>Location:</strong> {animal["locations"][0]}</li>'
    except KeyError:
        pass
    try:
        output += f'<li><strong>Type:</strong> {animal["characteristics"]["type"]}</li>'
    except KeyError:
        pass
    finally:
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
    animal_name = input("What animals do you want to display? ")
    animals_data = fetch_data(animal_name)
    content = get_info_for_each_animal(animals_data)
    code = content_temp('animals_template.html')
    if content != "":
        new_code = code.replace('__REPLACE_ANIMALS_INFO__', content)
    else:
        new_code = code.replace('__REPLACE_ANIMALS_INFO__', f"<h2> The animal {animal_name} doesn't exist.</h2>")
    write_new_html(new_code)


if __name__ == "__main__":
    main()
