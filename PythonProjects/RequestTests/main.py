import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'trainer_token'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '13517' 
body_CREATE = { 
    "name": "Belatrisa",
    "photo_id": -1
    }
body_CHANGE = {
    "pokemon_id": "188242",
    "name": "Barahlush",
    "photo_id": 7
}
body_CATCH = {
    "pokemon_id": "188242"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_CREATE)
print(response_create.text)'''

'''response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_CHANGE)
print(response_change.text)'''

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_CATCH)
print(response_catch.text)

