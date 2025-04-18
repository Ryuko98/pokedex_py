from models.pokemon_model import get_pokemon_data

def find_pokemon(name):
    if not name or not name.strip():
        return None, "Debes ingresar un nombre o índice de Pokémon."

    name = name.strip().lower()
    pokemon = get_pokemon_data(name)
    if pokemon:
        return pokemon, None
    else:
        return None, f"No se encontró el Pokémon: '{name}'."
