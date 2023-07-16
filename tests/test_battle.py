from pokemon_battle.battle_logic import (
    select_move,
    calculate_damage,
    get_type_effectiveness,
    fetch_move_data,
)


def test_select_move():
    pokemon = {
        'moves': ['mega-punch']
    }

    move = select_move(pokemon)

    assert move['name'] in pokemon['moves']
    assert move['type'] == 'normal'
    assert move['power'] == 80
    assert move['accuracy'] == 85
    assert move['pp'] == 20

def test_calculate_damage():
    attacker = {
        'stats': [{'name': 'attack', 'value': 50}],
    }
    defender = {
        'stats': [{'name': 'defense', 'value': 30}],
        'types': ['Fire']
    }
    move = {
        'power': 60,
        'type': 'Fire'
    }

    damage = calculate_damage(attacker, defender, move)

    assert 80 <= damage <= 100

def test_get_type_effectiveness():
    move_type = 'fire'
    defender_types = ['water']

    effectiveness = get_type_effectiveness(move_type, defender_types)

    assert effectiveness == 0.5

def test_fetch_bad_move_data():
    move_name = 'move1'
    
    move_data = fetch_move_data(move_name)

    assert move_data is None

