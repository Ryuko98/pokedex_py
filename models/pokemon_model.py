from models.pokeapi import obtener_pokemon

def obtener_datos(nombre):
    datos = obtener_pokemon(nombre)
    if not datos:
        return None

    return {
        'name': datos['name'].capitalize(),
        'id': datos['id'],
        'height': datos['height'],
        'weight': datos['weight'],
        'sprites': datos['sprites']['front_default'],
        'types': [tipos.get(t['type']['name'], t['type']['name'].capitalize()) for t in datos['types']]
    }

tipos = {
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