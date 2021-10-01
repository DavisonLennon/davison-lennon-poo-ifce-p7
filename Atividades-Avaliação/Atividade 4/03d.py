# 03d.py: questao 3d

import math

class Ponto():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def distancia_da_origem(self):
        dx = self.__x
        dy = self.__y

        return math.sqrt(dx**2 + dy**2) 
