
import json
from requests import get
from flask import Flask, render_template

def get_pokemon_name(id):


    url = 'https://pokeapi.co/api/v2/pokemon/' + str(id) 
    poke = get(url)
    data = poke.json()
    name = data['name']
    return name

def get_class_pokemon(id):
    url = 'https://pokeapi.co/api/v2/pokemon/' + str(id)
    poke = get(url)
    data = poke.json()
    class_list = []
    for poke_class in data['types']:
        class_list.append(poke_class['type']['name'])
    return class_list

def get_poke_by_class(classP):
    url = 'https://pokeapi.co/api/v2/type/' + classP
    pokes = get(url)
    pokemons_in_class = pokes.json()['pokemon']
    return pokemons_in_class
