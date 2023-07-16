import pytest
from pokemon_battle.models import db, Pokemon
from pokemon_battle.database import store_pokemon_to_db, get_pokemon_from_db
from ast import literal_eval

@pytest.fixture
def setup_database():
    # Set up a test database and create the necessary tables
    db.create_all()
    yield
    # Clean up the test database
    db.session.remove()
    db.drop_all()

def test_store_pokemon_to_db(setup_database):
    # Prepare test data
    pokemon_info = {
        'name': 'Pikachu',
        'types': ['Electric'],
        'stats': [{'name': 'HP', 'value': 55}, {'name': 'Attack', 'value': 40}],
        'abilities': ['Static', 'Lightning Rod'],
        'moves': ['Thunderbolt', 'Quick Attack']
    }

    # Call the function to store the Pokémon
    store_pokemon_to_db(pokemon_info)

    # Retrieve the stored Pokémon from the database
    pokemon = Pokemon.query.filter_by(name='Pikachu').first()

    # Assert that the stored Pokémon matches the input data
    assert pokemon is not None
    assert pokemon.name == pokemon_info['name']
    assert literal_eval(pokemon.types) == pokemon_info['types']
    assert literal_eval(pokemon.stats) == pokemon_info['stats']
    assert literal_eval(pokemon.abilities) == pokemon_info['abilities']
    assert literal_eval(pokemon.moves) == pokemon_info['moves']

def test_get_pokemon_from_db(setup_database):
    # Prepare a Pokémon record in the database
    pokemon = Pokemon(
        name='Pikachu',
        types=str(['Electric']),
        stats=str([{'name': 'HP', 'value': 55}, {'name': 'Attack', 'value': 40}]),
        abilities=str(['Static', 'Lightning Rod']),
        moves=str(['Thunderbolt', 'Quick Attack'])
    )
    db.session.add(pokemon)
    db.session.commit()

    # Call the function to get the Pokémon information
    pokemon_info = get_pokemon_from_db('Pikachu')

    # Assert that the retrieved Pokémon information matches the database record
    assert pokemon_info is not None
    assert pokemon_info['name'] == 'Pikachu'
    assert pokemon_info['types'] == ['Electric']
    assert pokemon_info['stats'] == [{'name': 'HP', 'value': 55}, {'name': 'Attack', 'value': 40}]
    assert pokemon_info['abilities'] == ['Static', 'Lightning Rod']
    assert pokemon_info['moves'] == ['Thunderbolt', 'Quick Attack']