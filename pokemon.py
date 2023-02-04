import random
import requests
import statistics

from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/pokemon', methods=['GET'])
def get_pokemon_details():
    favorite_pokemon_dict = {
        'dragonair': 148,
        'charizard': 6,
        'gengar': 94,
        'probopass': 476,
        'umbreon': 197
    }

    # Make a GET request to the PokeAPI to retrieve the details for each pokemon
    pokemon = []
    base_happiness = []
    for name, id in favorite_pokemon_dict.items():
        pokemon_details = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}').json()
        pokemon_species_details = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{id}/').json()

        # Keep base happiness of all 5 fav pokemon to calculate avg and median later
        base_happiness.append(pokemon_species_details['base_happiness'])

        # Add the extracted attributes to the list of pokemons
        pokemon.append({
            'name': pokemon_details['name'],
            'height': pokemon_details['height'],
            'weight': pokemon_details['weight'],
            'color': pokemon_species_details['color']['name'],
            'moves': random.sample([move['move']['name'] for move in pokemon_details['moves']], 2),
            'base_happiness': pokemon_species_details['base_happiness']
        })

    # Assume we are calculating the average and median base happiness of the 5 fav pokemon
    avg_base_happiness = statistics.mean(base_happiness)
    median_base_happiness = statistics.median(base_happiness)

    # Return the list of pokemons as a JSON response
    return jsonify({
        'pokemon': pokemon,
        'average_base_happiness': avg_base_happiness,
        'median_base_happiness': median_base_happiness
    })

if __name__ == '__main__':
    app.run(debug=True)
