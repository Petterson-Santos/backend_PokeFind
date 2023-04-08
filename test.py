from Pokemon import Pokemon
from Pokedex import Pokedex
import list_pokemon
import random

pokedex = Pokedex()

pokemon_name = list_pokemon.lista[random.randint(0, 250)]
pokemon_random = pokedex.get_my_pokemon(pokemon_name)

pokemon_name = input('Digite o nome do pokemon: ')
pokemon_input = pokedex.get_my_pokemon(pokemon_name)

pokemon_input.show()
print()
pokemon_random.show()