import requests

#Request the data from the pokeapi
def request(poke_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{poke_name.lower()}/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return Exception
