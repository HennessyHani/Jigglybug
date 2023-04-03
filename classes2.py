from abc import ABC, abstractmethod

class Bird(ABC):
    energy = 1

    @abstractmethod
    def fly(self):
        pass


class Owl(Bird):
    def fly(self):
        self.energy += -1
    
    def eat(self):
        self.energy += 1


class Dodo(Bird):
    def fly(self):
        self.energy += -5

    def eat(self):
        self.energy += 3

Gary = Owl()
print(Gary.energy)
Gary.eat()
print(Gary.energy)

Squeak = Dodo()
print(Squeak.energy)
Squeak.eat()
print(Squeak.energy)