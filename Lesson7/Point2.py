from abc import ABC, abstractmethod

class AClothes(ABC):
    @abstractmethod
    def calc(self):
        pass

class Coat(AClothes):
    def __init__(self, v):
        self.__v = v
    def calc(self):
        return self.__v / 6.5 + 0.5

    @property
    def coat_param(self):
        return self.__v

class Costume(AClothes):
    def __init__(self, h):
        self.__h = h
    def calc(self):
        return 2 * self.__h + 0.3

    @property
    def costume_param(self):
        return self.__h


coat = Coat(13)
print(coat.calc())
print(coat.coat_param)

costume = Costume(3)
print(costume.calc())
print(costume.costume_param)
