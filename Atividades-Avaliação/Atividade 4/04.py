# 04.py: questao 4

import math

class Ponto():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, valor):
        self.__x = valor

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, valor):
        self.__y = valor

class Reta():
    def __init__(self, ponto_a, ponto_b):
        self.__a = ponto_a
        self.__b = ponto_b

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, ponto):
        self.__a = ponto

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, ponto):
        self.__b = ponto

    def distancia(self):
        dx = self.__a.__x - self.__b.__x
        dy = self.__a.__y - self.__b.__y

        return math.sqrt(dx**2 + dy**2)

