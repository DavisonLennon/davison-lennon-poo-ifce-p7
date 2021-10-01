# 03f.py: questao 3f

class Ponto():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

class Retangulo():
    def __init__(self, x1, y1, x2, y2):
        self.__p1 = Ponto(x1, y1)
        self.__p2 = Ponto(x2, y2)
