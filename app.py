from flask import Flask, render_template, request
from controllers.pokemon_controller import find_pokemon

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    pokemon = None
    error = None

    if request.method == 'POST':
        nombre = request.form.get('pokemon_name')
        pokemon, error = find_pokemon(nombre)

    return render_template('index.html', pokemon=pokemon, error=error)

if __name__ == '__main__':
    app.run(debug=True)
