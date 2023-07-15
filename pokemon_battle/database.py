from pokemon_battle.models import db, Pokemon
from ast import literal_eval

def store_pokemon_to_db(pokemon_info):
    pokemon = Pokemon(
        name=pokemon_info['name'],
        types=str(pokemon_info['types']),
        stats=str(pokemon_info['stats']),
        abilities=str(pokemon_info['abilities']),
        moves=str(pokemon_info['moves'])
    )
    db.session.add(pokemon)
    db.session.commit()

def get_pokemon_from_db(name):
    pokemon = Pokemon.query.filter_by(name=name).first()
    pokemon_info = None

    if pokemon:
        # If the Pokémon information is already in the database, retrieve it from there
        pokemon_info = {
            'name': pokemon.name,
            'types': [name for name in literal_eval(pokemon.types)],
            'stats': [{'name': stat['name'], 'value': stat['value']} for stat in literal_eval(pokemon.stats)],
            'abilities': [ability for ability in literal_eval(pokemon.abilities)],
            'moves': [move for move in literal_eval(pokemon.moves)]
        }
    
    return pokemon_info