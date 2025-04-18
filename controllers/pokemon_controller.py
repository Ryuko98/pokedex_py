from models.pokemon_model import obtener_datos

def buscar_pokemon(nombre):
    if not nombre:
        return None, "Debes ingresar un nombre de Pokémon."

    pokemon = obtener_datos(nombre)
    if pokemon:
        return pokemon, None
    else:
        return None, f"No se encontró el Pokémon: '{nombre}'."
