class Animal:
    def speak(self):
        print('发出动物的叫声')

class Dog(Animal):
    def speak(self):
        print('汪汪汪！')

class Cat(Animal):
    def speak(self):
        print('喵喵喵！')

def make_sound(animal: Animal):
    animal.speak()


make_sound(Animal())
make_sound(Dog())
make_sound(Cat())
