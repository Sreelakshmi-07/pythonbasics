# class (design,blueprint)
# object (entity)
# reference ro perform operations on object
# self instance keyword
class Person:
    def walk(self):   #method 1
        print("Person is walking")
    def read(self):   #method 2
        print("person is reading")
pe = Person()   #object creation
pe.walk()
pe.read()