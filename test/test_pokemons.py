import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'
token = '2dd0d333280368fd626aa66cb125583f'

def test_status_code():
    response = requests.get(f'{host}/trainers', params={'level': 1})
    assert response.status_code == 200

def test_my_name():
    response = requests.get(f'{host}/trainers', params= {'trainer_id': 2519 })
    assert response.json()['trainer_name']== 'Natali'