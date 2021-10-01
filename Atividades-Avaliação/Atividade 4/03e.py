# 03e.py: questao 3e

import math

class Ponto():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def argumento(self):
        dx = self.__x
        dy = self.__y

        return math.atan2(dy, dx)
