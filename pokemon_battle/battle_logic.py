import random
import requests

def simulate_battle_logic(pokemon1, pokemon2):
    # Print the battle starting message
    print("A battle begins between", pokemon1['name'], "and", pokemon2['name'])

    # Initialize the battle state
    current_pokemon1 = pokemon1
    current_pokemon2 = pokemon2

    # Retrieve the hp and speed attributes from the stats dictionary
    for stat in current_pokemon1['stats']:
        if stat['name'] == 'hp':
            current_pokemon1['hp'] = stat.get('value', 0)
        elif stat['name'] == 'speed':
            current_pokemon1['speed'] = stat.get('value', 0)

    for stat in current_pokemon2['stats']:
        if stat['name'] == 'hp':
            current_pokemon2['hp'] = stat.get('value', 0)
        elif stat['name'] == 'speed':
            current_pokemon2['speed'] = stat.get('value', 0)

    # Loop until one of the Pokémon faints
    while current_pokemon1['hp'] > 0 and current_pokemon2['hp'] > 0:
        # Determine the turn order based on the Pokémon's speed
        if current_pokemon1['speed'] > current_pokemon2['speed']:
            first_pokemon = current_pokemon1
            second_pokemon = current_pokemon2
        else:
            first_pokemon = current_pokemon2
            second_pokemon = current_pokemon1

        # First Pokémon's turn
        execute_move(first_pokemon, second_pokemon)

        # Check if the second Pokémon faints
        if second_pokemon['hp'] <= 0:
            break

        # Second Pokémon's turn
        execute_move(second_pokemon, first_pokemon)

    # Determine the winner and print the result
    if current_pokemon1['hp'] > 0:
        winner = current_pokemon1
    else:
        winner = current_pokemon2

    print("The battle is over! The winner is", winner['name'])

    return winner

def execute_move(attacker, defender):
    # Select a move for the attacker
    move = select_move(attacker)

    # Print the move being used
    print(attacker['name'], "uses", move['name'])

    # Calculate the damage inflicted
    damage = calculate_damage(attacker, defender, move)

    # Apply the damage to the defender's HP
    defender['hp'] -= damage

    # Print the damage dealt
    print(defender['name'], "loses", damage, "HP")

def select_move(pokemon):
    # Get a random move from the available moves
    random_move = random.choice(pokemon['moves'])

    # Fetch additional move data from the PokeAPI
    move_data = fetch_move_data(random_move)

    # Return the selected move with additional data
    return {
        'name': move_data['name'],
        'type': move_data['type']['name'],
        'power': move_data['power'],
        'accuracy': move_data['accuracy'],
        'pp': move_data['pp']
    }

def calculate_damage(attacker, defender, move):
    # Extract relevant attributes from the attacker and defender
    for stat in attacker['stats']:
        if stat['name'] == 'attack':
            attacker_attack = stat['value']
    for stat in defender['stats']:
        if stat['name'] == 'defense':
            defender_defense = stat['value']
    move_power = move.get('power', 0)
    if not move_power:
        move_power = 0
    move_type = move['type']

    type_effectiveness = get_type_effectiveness(move_type, defender['types'])

    # Calculate damage using a simplified formula
    damage = (attacker_attack / defender_defense) * move_power * type_effectiveness

    # Apply random variation to damage (within a certain range)
    random_variation = random.uniform(0.85, 1.0)
    damage = damage * random_variation

    # Check move accuracy and determine if the move hits the target
    if 'accuracy' in move and move['accuracy'] is not None:
        hit_chance = move['accuracy'] / 100.0
        if random.random() <= hit_chance:
            # Move hits the target
            return int(damage)
        else:
            # Move misses the target
            return 0
    else:
        # Move has no accuracy value, always hits
        return int(damage)
    
def get_type_effectiveness(move_type, defender_types):
    # Define type effectiveness values (basic values)
    type_effectiveness_chart = {
        'normal': {'normal': 1.0, 'fire': 1.0, 'water': 1.0, 'grass': 1.0, 'electric': 1.0},
        'fire': {'normal': 1.0, 'fire': 0.5, 'water': 0.5, 'grass': 2.0, 'electric': 1.0},
        'water': {'normal': 1.0, 'fire': 2.0, 'water': 0.5, 'grass': 0.5, 'electric': 1.0},
        'grass': {'normal': 1.0, 'fire': 0.5, 'water': 2.0, 'grass': 0.5, 'electric': 1.0},
        'electric': {'normal': 1.0, 'fire': 1.0, 'water': 2.0, 'grass': 0.5, 'electric': 0.5}
    }

    # Calculate type effectiveness based on the move type and defender's types
    # Default effectiveness
    effectiveness = 1.0

    for defender_type in defender_types:
        if move_type in type_effectiveness_chart and defender_type in type_effectiveness_chart[move_type]:
            effectiveness *= type_effectiveness_chart[move_type][defender_type]

    return effectiveness

def fetch_move_data(move_name):
    try:
        response = requests.get(f'https://pokeapi.co/api/v2/move/{move_name}')
        response.raise_for_status()  # Raise an exception for non-2xx status codes

        move_data = response.json()

        return move_data

    except requests.exceptions.RequestException as e:
        # Handle request-related exceptions
        print(f"Error during API request: {e}")

    except KeyError as e:
        # Handle key error if required data is missing in the response
        print(f"KeyError: {e}")

    except ValueError as e:
        # Handle value error if there's an issue with the response data
        print(f"ValueError: {e}")

    except Exception as e:
        # Handle other unexpected exceptions
        print(f"An error occurred: {e}")

    return None