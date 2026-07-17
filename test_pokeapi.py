from services.pokemon.pokeapi_service import PokeApiService


pokeapi = PokeApiService()

while True:
    name = input("Pokémon: ")

    pokemon = pokeapi.get_pokemon(name)

    if not pokemon:
        print("Não encontrei esse Pokémon.")
        continue

    print(pokemon)