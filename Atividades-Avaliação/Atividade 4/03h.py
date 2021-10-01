# 03h.py: questao 3h

class Locomotiva():
    def __init__(self, c, a, p):
        self.__comprimento = c
        self.__altura = a
        self.__potencia = p

class Vagao():
    def __init__(self, c, a):
        self.__comprimento = c
        self.__altura = a

class Trem():
    def __init__(self, loc, vag):
        self.__locomotiva = loc
        self.__vagao = vag

