class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")




animal=Animal("generic animal")
#animal.speak()            
print(animal.speak())


dog=Dog("Buddy")
dog.speak()


class Father:
    def cricket(self):
        print("Playing cricket 🏏")

class Mother:
    def cooking(self):
        print("Cooking food 🍳")

class Child(Father, Mother):    # two parents!
    def studying(self):
        print("Studying 📚")


child = Child()
child.cricket()    # from Father ✅
child.cooking()    # from Mother ✅
child.studying()   # own method ✅        