import requests
from Pokemon import Pokemon

class Pokedex():
    def __init__(self):
        pass

    def get_pokemon(self, pokemon_name):
        api = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
        res = requests.get(api)
        poke = res.json()
        return poke

    def get_gen(self, poke):
        first_game = poke['game_indices'][0]['version']['name']
    
        if first_game == 'red' or first_game == 'blue' or first_game == 'yellow':
            return 1
        elif first_game == 'gold' or first_game == 'silver' or first_game == 'crystal':
            return 2
        else:
            return 3

    def get_name(self, poke):
        return poke['name']

    def get_type(sellf,poke, j):
        types = []
        for i in poke['types']:
            types.append(i['type']['name'])
            j += 1
        
        if j == 1:
            types.append("")
            types[1] = types[0]

        return types

    def get_height(self, poke):
        return poke['height']/10

    def get_weight(self, poke):
        return poke['weight']/10

    def get_my_pokemon(self, pokemon_name):
        poke = self.get_pokemon(pokemon_name)
        types = []
        types = self.get_type(poke, 0)
        pkm = Pokemon(self.get_name(poke), self.get_gen(poke), str(types[0]), str(types[1]), self.get_height(poke), self.get_weight(poke))
        
        return pkm
    
    