from flask import Blueprint, jsonify, request
from .database import store_pokemon_to_db, get_pokemon_from_db
from .battle_logic import simulate_battle_logic
import requests

api = Blueprint('api', __name__)

@api.route('/pokemon/<name>', methods=['GET'])
def get_pokemon_info(name):
    # Fetch Pokémon information
    pokemon_info = fetch_pokemon_info(name)

    if not pokemon_info:
        return jsonify({'error': 'Failed to fetch Pokémon information.'}), 404
        
    return jsonify(pokemon_info)

@api.route('/pokemon/battle', methods=['POST'])
def simulate_battle():
    data = request.get_json()
    pokemon1_name = data.get('pokemon1')
    pokemon2_name = data.get('pokemon2')

    # Fetch Pokémon data from the database or API based on the names
    pokemon1 = fetch_pokemon_info(pokemon1_name)
    pokemon2 = fetch_pokemon_info(pokemon2_name)

    # Check if the Pokémon data exists
    if not pokemon1 or not pokemon2:
        return jsonify({'error': 'Pokémon not found.'}), 404

    # Perform battle calculations and determine the winner
    winner = simulate_battle_logic(pokemon1, pokemon2)

    # Return the battle result as a JSON response
    result = {
        pokemon1_name: pokemon1,
        pokemon2_name: pokemon2,
        'winner': winner['name']
    }

    return jsonify(result)

def fetch_pokemon_info(name):
    # Check if the Pokémon information is already in the database
    pokemon_info = get_pokemon_from_db(name)
    
    if not pokemon_info:
        # If the Pokémon information is not in the database, fetch it from the PokeAPI
        pokemon_info = retrieve_pokemon_from_pokeapi(name)

        if pokemon_info:
            # Store the Pokémon in the database
            store_pokemon_to_db(pokemon_info)

    return pokemon_info

def retrieve_pokemon_from_pokeapi(name):
        
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')

    if response.status_code != 200:
        return None

    pokemon_data = response.json()

    # Transform the PokeAPI response into a JSON response for the client
    pokemon_info = {
        'name': pokemon_data['name'],
        'types': [type_data['type']['name'] for type_data in pokemon_data['types']],
        'stats': [{'name': stat_data['stat']['name'], 'value': stat_data['base_stat']} for stat_data in pokemon_data['stats']],
        'abilities': [ability_data['ability']['name'] for ability_data in pokemon_data['abilities']],
        'moves': [move_data['move']['name'] for move_data in pokemon_data['moves']]
    }

    return pokemon_info