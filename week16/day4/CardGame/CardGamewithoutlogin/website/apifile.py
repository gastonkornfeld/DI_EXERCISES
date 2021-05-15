

import random
from requests import get
# using only the characters that i try before and are working in the api
characters = ['Bender', 'Fry', 'Leela', 'Amy', 'Hermes', 'Kif']

def get_character(name):

    url = 'http://futuramaapi.herokuapp.com/api/v2/characters?search=' + name


    character = get(url)



    return character.json()[0]

def get_name(name):
    character = get_character(name)
    name = character['Name']
    return name


def get_species(name):
    character = get_character(name)
    specie = character['Species']
    return specie

def get_age(name):
    character = get_character(name)
    age = character['Age']
    return age

def get_planet_of_charac(name):
    character = get_character(name)
    planet = character['Planet']
    return planet

def get_profession(name):
    character = get_character(name)
    profession = character['Profession']
    return profession


def get_pic_url(name):
    character = get_character(name)
    url = character['PicUrl']
    return url




def set_random_rarity():
    """
    function that set rarity in 2% for legendary, 10% for epic, 20% for rare and %68 for common cards 
    return a list with the words described to use random.choice on it when create a card rarity
    """
    list_of_rarity = []
    for i in range(60):
        list_of_rarity.append('COMMON')
    for i in range(24):
        list_of_rarity.append('RARE')
    for i in range(14):
        list_of_rarity.append('EPIC')
    for i in range(40):
        list_of_rarity.append('LEGENDARY')
    choice = random.choice(list_of_rarity)
    print('choice made')
    
    return choice






