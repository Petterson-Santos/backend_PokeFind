from Pokedex import Pokedex
import list_pokemon
import random

# instacia a pokedex, que e o controlador do comparador e o gerador de pokemon
pokedex = Pokedex()

# pega o nome do pokemon randomico a partir da lista de nomes e gera um pokemon a partir desse nome na api 
pokemon_name = list_pokemon.lista[random.randint(0, 250)]
pokemon_random = pokedex.get_my_pokemon(pokemon_name)
# usar para testar 
pokemon_random.show()

# carrega um valor padrao para pokemon para cair no loop
pokemon_name = ''

# loop da aplicacao
while pokemon_name != pokemon_random.name: 
    pokemon_name = input('Digite o nome do pokemon: ')
    try:
        pokemon_input = pokedex.get_my_pokemon(pokemon_name)
    except: # caso o nome informado no input nao exista, cai na except abaixo
        print()
        print('Error: O nome do pokemon informado esta incorreto!')
        print()
    else:
        print()
        message = pokedex.compare_pokemon(pokemon_input, pokemon_random)
        print(message)
        print()
