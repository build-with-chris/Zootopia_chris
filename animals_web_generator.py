import json

def load_data(filepath):
    with open(filepath, "r") as handle:
        return json.load(handle)


def get_info_for_each_animal(animals_data):
    for animal in animals_data:
        print(f'Name: {animal['name']}')
        print(f'Diet: {animal['taxonomy']['order']}')
        print(f'Location: {animal['locations'][0]}')
        try:
            print(f'Type: {animal['characteristics']['type']}')
        except KeyError:
            print()
            continue

        print()


def main():
    animals_data = load_data('animals_data.json')
    get_info_for_each_animal(animals_data)

if __name__ == "__main__":
    main()
