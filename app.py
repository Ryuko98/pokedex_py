from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Aquí se puede incluir la lógica de la Pokédex, por ejemplo, el nombre del Pokémon
    pokemon_name = "Pikachu"
    return render_template('index.html', pokemon_name=pokemon_name)

if __name__ == '__main__':
    app.run(debug=True)
