# for abstract class method import abstractmethod
from abc import ABCMeta,abstractmethod
#the metaclass and abstractmethod is used to tell example:user to use printarea if they have have not used
class shape(metaclass=ABCMeta):
    @abstractmethod
    def printarea(self):
        return 0
class rectangle(shape):
    side=4
    type="rectangle"
    def __init__(self):
        self.length=4
        self.breadth=3
    def printarea(self):
        return self.length*self.breadth
class  sqaure(shape):
    side=4
    type="rectangle"
    def __init__(self):
        self.s=4
    def printarea(self):
        return self.s*self.self.s
rect1=rectangle()
sq=sqaure()
print(rect1.printarea())
print(sq.printarea())