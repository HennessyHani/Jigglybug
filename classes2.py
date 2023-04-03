from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod

    energy = 1 

    def fly(self):
        pass


class Owl(Bird):
    def fly(self):
        self.energy = -1
    
    def eat(self):
        self.energy = 1


class Dodo(Bird):
    def fly(self):
        self.energy = -5

    def eat(self):
        self.energy = 3

Gary = Owl()
print(Gary.energy())

Sqeauk = Dodo()
print()