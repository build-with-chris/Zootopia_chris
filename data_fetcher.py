import requests
from plotly.figure_factory.utils import list_of_options

NAME = 'fox'
Key = "OraJs8wSoCxsuaSufdDG5A==geBlmOnQQKafik7c"
URL = 'https://api.api-ninjas.com/v1/animals?name={}'.format(NAME)


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    """
    response = requests.get(URL, headers={'X-Api-Key': Key})
    if response.status_code == requests.codes.ok:
        list_of_type = response.json()
    else:
        print("Error:", response.status_code, response.text)
    output_list = []
    for animal in list_of_type:
        if animal_name.lower() in animal['name'].lower():
            output_list.append(animal)
    return output_list



    # for animal in list_of_type:
    #     animal_dict = {}
    #     if animal_name in animal['name']:
    #         animal_dict["name"] = (animal["name"])
    #         animal_dict["taxonomy"] = (animal['taxonomy']['order'])
    #         animal_dict["location"] = (animal['locations'][0])
    #         try:
    #             animal_dict["type"] = (animal['characteristics']['type'])
    #             print()
    #         except KeyError:
    #             print()
    #     return animal_dict

print(fetch_data("Fox"))