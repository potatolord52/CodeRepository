class Animal():
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age

    def getName(self):
        return self.name
    def getGender(self):
        return self.gender
    def getAge(self):
        return self.age

class Mammal(Animal):
    def __init__(self,name,gender,age,family):
        self.family=family
    def getFamily(self):
        return self.family

class Insect(Animal):
    def __init__(self,name,gender,age,family,skeFeat):
        self.family=family
        self.skeFeat=skeFeat
    def getFamily(self):
        return self.family
    def getSke(self):
        return self.skeFeat

class Dog(Mammal):
    def __init__(self,name,gender,age,family,breed):
        self.breed=breed
    def getBreed(self):
        return self.breed

class Bee(Insect):
    def __init__(self,name,gender,age,family,skeFeat,breed):
        self.breed=breed
    def getBreed(self):
        return self.breed

tom=Mammal("Tom","M",14,"felidae")
print(tom.getFamily())

beetle1=Insect("Beetle1","M",2,"apidae","N")
print(beetle1.getSke())
