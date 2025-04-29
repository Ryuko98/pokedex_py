from flask import Flask, render_template, request
from controllers.pokemon_controller import find_pokemon, find_region

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", active_page="home")

@app.route('/', methods=['GET', 'POST'])
def index():
    pokemon = None
    region = None
    error = None

    if request.method == 'POST':
        search_type = request.form.get('search_type')
        query = request.form.get('query')
        
        if search_type == 'pokemon':
            pokemon, error = find_pokemon(query)
        elif search_type == 'region':
            region, error = find_region(query)

    return render_template('index.html', pokemon=pokemon, region=region, error=error)

if __name__ == '__main__':
    app.run(debug=True)
