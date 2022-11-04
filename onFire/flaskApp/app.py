from flask import Flask
import pokebase as pb
import random

app = Flask(__name__)

@app.route('/')
def index():
    pokemon=pb.pokemon(random.randint(1,151))
    return {
        "number": pokemon.id,
        "name": pokemon.name
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
