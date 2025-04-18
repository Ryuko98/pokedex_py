from models.pokemon_model import get_pokemon_data, get_region_data

def find_pokemon(name):
    if not name or not name.strip():
        return None, "Debes ingresar un nombre o índice de Pokémon."

    name = name.strip().lower()
    pokemon = get_pokemon_data(name)
    if pokemon:
        return pokemon, None
    else:
        return None, f"No se encontró el Pokémon: '{name}'."

def find_region(name):
    if not name or not name.strip():
        return None, "Debes ingresar un nombre o índice de región."

    name = name.strip().lower()
    region = get_region_data(name)
    if region:
        return region, None
    else:
        return None, f"No se encontró la región: '{name}'."
