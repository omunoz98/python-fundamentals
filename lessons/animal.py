# abstract base classes exist using an import called ABC (helper)
# abstract classes can not be instantiate in python
# abstract methods can be called by its subclass
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, family):
        self._family = family


    @abstractmethod
    def info(self):
        pass

    def make_sound(self):
        return 'RUMBLE goes the {}'.format(self._family)

    def __str__(self):
        return self._family

class Dog(Animal):
    def __init__(self, name):
        super().__init__('Canine')
        self._name = name

    def info(self):
        return 'My dog\'s name is {0} and he is a {1}'\
            .format(self._name, self.family)
    def make_soud(self):
        return 'barks'


class frog(Animal):
    def __init__(self, name):
        super().__init__('Amphibian')
        self._name = name

    def info(self):
        return 'My frog\'s name is {0} and he is a {0}'\
            .format(self._name, self._family)


dog1 = Dog('Lucky')
frog = frog('George')
test = Animal('Mammal')
print(dog1.info())
print(frog.info())
# print(test.make_sound())

