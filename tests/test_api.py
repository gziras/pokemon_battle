from flask import jsonify

def test_get_pokemon_info(client):
    response = client.get('/pokemon/charizard')
    data = response.get_json()

    assert response.status_code == 200
    assert 'name' in data
    assert 'types' in data
    assert 'stats' in data
    assert 'abilities' in data
    assert 'moves' in data

def test_get_pokemon_info_not_found(client):
    response = client.get('/pokemon/unknown')
    data = response.get_json()

    assert response.status_code == 404
    assert 'error' in data

def test_simulate_battle(client):
    data = {
        'pokemon1': 'charizard',
        'pokemon2': 'blastoise'
    }
    response = client.post('/pokemon/battle', json=data)
    result = response.get_json()

    assert response.status_code == 200
    assert 'winner' in result
    assert 'charizard' in result
    assert 'blastoise' in result

def test_simulate_battle_pokemon_not_found(client):
    data = {
        'pokemon1': 'charizard',
        'pokemon2': 'unknown'
    }
    response = client.post('/pokemon/battle', json=data)
    result = response.get_json()

    assert response.status_code == 404
    assert 'error' in result
