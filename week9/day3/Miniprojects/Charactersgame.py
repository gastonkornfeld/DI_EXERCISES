


# Description
# Create a Character class with the following attributes and methods:
# name
# life – starts at 20 for all
# attack – the base attack for this character (integer), default 10
# basic_attack() - accepts another character as a parameter and does to the other characters
# Instructions
# Now create 3 different classes that inherit from Character:
# Every character type should say (print) something else when they are created, get creative :)


class Character():

    def __init__(self, name):
        self.name = name
        self.atack = 10
        self.life = 20
        


    def basic_atack(self, other):
        other.atack -= 10
        print(f"this basic atack took 10 points atack from {other.name} now his atack is {other.atack}")
        


# Druid:
# meditate() - increase life by 10, decrease attack by 2
# animal_help()- increase attack by 5
# fight() - accepts another character as a parameter, does (0.75life + 0.75attack) to the other character
# Example: 
# druid.fight(other_char): other_char.life - (0.75*druid.life + 0.75*druid.attack)

class Druid(Character):

    def __init__(self, name):
        super().__init__(name)
        self.life = 20
        self.atack = 10
        print(f"{self} Created. \n You are ready to fight the dark demonds")
        
    def meditate(self):
        self.life += 10
        self.atack -= 2
        print(f"{self.name} meditates. \nThe life of {self.name} increase to {self.life}, atack decrease to {self.atack}")
    
    def animal_help(self):
        self.atack += 5
        print(f"{self.name} invoque animal help. \n The atack of {self.name} increase to {self.atack}")
    
    def fight(self, other):
        other.life = other.life - int(0.75 * self.life + 0.75 * self.atack) 
        print(f"{self.name} fight {other.name}. \n The life of {other.name} decrease to {other.life}")
    
    def __repr__(self):
        return f"Druid {self.name} life: {self.life}, atack power: {self.atack}"




# Warrior:
# brawl() - accepts another character as a parameter,
# does (2attack) to the other character and (0.5attack) to yourself
# train() - increase own attack and life by 2 each
# roar() - accepts another character as a parameter, decrease their attack by 3
class Warrior(Character):
    
    def __init__(self, name):
        super().__init__(name)
        self.life = 20
        self.atack = 10
        print(f"{self} Created.\n You are ready to defeat the lord of the rings")

    def brawl(self, other):
        print(f"{self.name} brawl super strong to {other}")
        self.atack1(other)
        self.atack1(other)
        self.life -= int((0.75 * self.life + 0.75 * self.atack) / 2)
        print(f"The life of {self.name} decrease to {self.life} beacuse of the brawl")

    def atack1(self, other):
        other.life -= int(0.75 * self.life + 0.75 * self.atack)
        print(f"{self.name} atacks. \n The life of {other.name} decrease to {other.life}") 

    def train(self):
        self.life += 2
        self.atack += 2
        print(f"{self.name} trains. \n The life and atack of {self.name} increase to life:{self.life}, atack: {self.atack}")

    def roar(self, other):
        other.atack -= 3
        print(f"{self.name} roar. \nThe atack of {other.name} decrease to {other.atack}")

    def __repr__(self):
        return f"Warrior {self.name} life: {self.life}, atack power: {self.atack}"



# Mage:
# curse() – accepts another character as a parameter, decrease targets attack by 2
# summon() - increases attack attribute by 3
# cast_spell() - accepts another character as a parameter,
#  does attack/life of damage to the other character (eg if your attack is 20 and life is 5 you do 4 damage)
# Once all your classes are created start testing them,
#  create one of each character and use each of their methods



class Mage(Character):
    
    def __init__(self, name):
        super().__init__(name)
        self.life = 20
        self.atack = 10
        print(f"{self} Created. \n You are ready to cast infinite spells")

    def curse(self, other):
        other.atack -= 2
        print(f"{self.name} curse to {other.name}. \nThe atack of {other.name} decrease to {other.atack}")

    def summon(self):
        self.atack += 3
        print(f"{self.name} invoke summon. \nThe atack of {self.name} increase to {self.atack}")

    def cast_spell(self, other):
        damage = self.atack/self.life
        other.life -= damage
        print(f"{self.name} cast a spell. \nThe spell decrease  the damage of {other.name} by {damage} points. \n new life:{other.life}")

    def __repr__(self):
        return f"Mage {self.name} life: {self.life}, atack power: {self.atack}"


drud = Druid("gaston")
Warrior1 = Warrior("gaston")
mage1 = Mage("alisa")
druid1 = Druid("yuval")

print(mage1.life)
print(druid1.atack)
druid1.fight(mage1)
mage1.curse(druid1)
for i in range(15):

    mage1.summon()
    druid1.meditate()
    druid1.animal_help()
    drud.meditate()
    Warrior1.train()

Warrior1.brawl(mage1)
Warrior1.roar(drud)
drud.meditate()
druid1.meditate()
druid1.animal_help()
druid1.fight(drud)
druid1.basic_atack(mage1)