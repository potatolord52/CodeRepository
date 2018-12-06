class Student():
    def __init__(self, name, age):
        if (age < 18):
            print("Student %s is too young!" %name)
            raise Exception()
        else:
            print("Student %s successfully enrolled." %name)


class Pet():
    def __init__(self, name, species, dateOfBirth):
        print("Name: %s Species: %s" %(name, species))
        self.property1 = name + ", a " + species
        self.dateOfBirth = dateOfBirth

    def getAge(self):
        # calculate age
        return self.dateOfBirth
    
class Dog():
    age = 20

    def test(self, name):
        self.name = name
        return name

def testFunction(argument):
    print("Argument %s" %argument)

### this is where the program starts ###

student1 = Student("John", 23)
student2 = Student("Jim", 16)


houseCat = Pet("Alex", "cat", 1234567)
houseDog = Pet("Bully", "dog", 1234345)

print("object property: ", houseCat.getAge())
print(houseCat.property1)

testFunction("This is a test")

print("End program")

#print("Before loop")
#for i in range(10):
#    print("i: %d" %i)
#    print("Inside loop")
#print("After loop")

wuffi = Dog()
print(wuffi.test("test"))
print("Wuffis name: ", wuffi.name, wuffi.age)

pussInBoots = Pet()
