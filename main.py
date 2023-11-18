import requests

response_create = requests.post('https://api.pokemonbattle.me:9104/pokemons', json = {
    "name": "Толстяк",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}, headers = {'Content-Type': 'application/json', 'trainer_token': '2dd0d333280368fd626aa66cb125583f'})

print (response.text) 


response_new_name = requests.put('https://api.pokemonbattle.me:9104/pokemons', json = {
    "pokemon_id": "19826",
    "name": "Худяк",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}, headers = {'Content-Type': 'application/json', 'trainer_token': '2dd0d333280368fd626aa66cb125583f'})

print (response.text) 

response_catch = requests.post('https://api.pokemonbattle.me:9104//trainers/add_pokeball', json = {
    "pokemon_id": "19828"
}, headers = {'Content-Type': 'application/json', 'trainer_token': '2dd0d333280368fd626aa66cb125583f'})

print (response.text) 
