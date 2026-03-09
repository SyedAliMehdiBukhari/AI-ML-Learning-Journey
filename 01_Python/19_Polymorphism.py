class Animal:
    def speak(self):
        print("Animal is speaking")
    
    
class Dog(Animal):
    def speak(self):
        print("Dog is speaking: Woof Woof")
    

class Cat(Animal):
    def speak(self):
        print("Cat is speaking: Meow")
        
        
class_list = [Dog(), Cat(), Animal()]

for list in class_list:
    list.speak()

