

# Create a class Human, it has the following attributes:

# name (str)
# age (int)
# living_place (Building - Default is None)
# Add the move(self, building) method to the Human class, 
# it sets the living place of this human to the building and add this human to the building inhabitants.
# Add the construct(self, address) method to the City class, it adds a building at the referenced address.
# Add the info(self, address) method to the City class, 
# it displays the number of buildings and the mean age of the citizens.


class Human():

    def __init__(self, name, age):
        self. name = name
        self.age = age
        self. living_place = None

    def move(self, building):
        building.habitants.append(self)
        self.living_place = building
        

    def __repr__(self):
        return f"{self.name} age:{self.age}  "
# Create another class Building, it has the following attributes:

# address (str)
# inhabitants (List of Human objs - Default is empty)


class Building():

    def __init__(self, adress):
        self.adress = adress
        self.habitants = []

    def __repr__(self):
        return f"BUILDING {self.adress}.Habitants:{self.habitants}"

# Create a class City, it has the following attributes:

# name (str)
# buildings (List of Building objs - Default is empty)


class City():

    def __init__(self, name):
        self.name = name
        self.buildings = []
    
    def construct(self, adress):
        self.buildings.append(Building(adress))
        # print(self.buildings)
    def addBuild(self, building):
        
        self.buildings.append(building)
        # print(self.buildings)

    def info(self, chek_adress):
        total_age = 0
        for building in self.buildings:
            print(building)
            if building.adress == chek_adress:
                for i in range(len(building.habitants)):
                    human_age = building.habitants[i].age
                    total_age += human_age
                print(f"Average age in the building = {total_age/len(building.habitants)}")

    def __repr__(self):
        return f"{self.buildings}"

human1 = Human("gaston", 32)
human2 = Human("maria", 30)
human3 = Human("diego", 36)
human4 = Human("natalia", 33)
print(human1)
building1 = Building("siempre viva 322")
human1.move(building1)
human2.move(building1)
human3.move(building1)
human4.move(building1)
city1 = City("springfield")
church = Building("hertzel 4")
city1.construct("church")
city1.addBuild(building1)
city1.info("siempre viva 322")
print(city1)


