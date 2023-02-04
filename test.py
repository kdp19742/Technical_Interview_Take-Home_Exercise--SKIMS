import json
import requests


def test():
    pokemon_id = 1
    pokemon_details = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}')
    print(json.loads(pokemon_details.content))

if __name__ == '__main__':
    test()