from models.pokeapi import get_pokemon_data

def buscar_pokemon(nombre):
    if not nombre:
        return None, "Debes ingresar un nombre de Pokémon."

    data = get_pokemon_data(nombre)
    data['types'] = [tipo_traduccion.get(tipo, tipo.capitalize()) for tipo in data['types']]

    
    if data:
        return data, None
    else:
        return None, f"No se encontró el Pokémon '{nombre}'."

tipo_traduccion = {
    'fire': 'Fuego',
    'water': 'Agua',
    'grass': 'Planta',
    'electric': 'Eléctrico',
    'dragon': 'Dragón',
    'ground': 'Tierra',
    'fighting': 'Lucha',
    'psychic': 'Psíquico',
    'ghost': 'Fantasma',
    'dark': 'Siniestro',
    'fairy': 'Hada',
    'ice': 'Hielo',
    'rock': 'Roca',
    'steel': 'Acero',
    'bug': 'Bicho',
    'normal': 'Normal',
    'poison': 'Veneno',
    'flying': 'Volador'
}
