

import json
from requests import get
from flask import Flask, render_template
from function import get_class_pokemon, get_poke_by_class, get_pokemon_name



app = Flask(__name__)

@app.route('/pokemon/<id1>')
def pokemon(id1):
    id2 = id1
    pokemon_name = get_pokemon_name(id2)
    poke_classes = get_class_pokemon(id2)

    return render_template('pokemon.html', name = pokemon_name, clss = poke_classes, id1 = id1)

@app.route('/pokemon/bytype/<typeP>')
def by_type(typeP):
    pokemons_class = get_poke_by_class(typeP)

    return render_template('bytype.html', pokemons = pokemons_class, typeP = typeP)


@app.route('/pokemon/byname/<name>')
def by_name(name):
    return render_template('byname.html', name=name)


@app.route('/pokemon/bytype')
def by_type2():
    pokemons_class = get_poke_by_class("water")

    return render_template('bytype.html', pokemons = pokemons_class, typeP = "water")

@app.route('/pokemon')
def by_type3():
    pokemons_class = get_poke_by_class("grass")

    return render_template('bytype.html', pokemons = pokemons_class, typeP = "water")



@app.route('/')
def all_classes():
    return render_template('main.html')


@app.route('/pokemon/all')
def all_poke():
    pokemons_names = []
    pokemons_class = []
    for i in range(1,15):
        poke_name = get_pokemon_name(i)
        # print(poke_name)
        poke_class = get_class_pokemon(i)
        # print(poke_class)
        pokemons_names.append(poke_name)
        # print(pokemons_names)
        pokemons_class.append(poke_class)
        # print(pokemons_class)
    return render_template('all_pokemon.html', names=pokemons_names, classes= pokemons_class)



app.run(debug=True, port=5001)


# print(data['ability'][0]['name'])
# # print(data['base_experience'])
# print(data['species'])
# # print(data['sprites'])
# print(data['type'][0]['name'])
# print(data['weight'])
