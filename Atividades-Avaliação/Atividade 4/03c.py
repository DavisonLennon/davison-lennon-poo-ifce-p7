# 03b.py: questao 3c

class Ponto():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def imprime_posicao(self):
        print( "(" + str(self.__x) + "," + str(self.__y) + ")" )

class Circulo(Ponto):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.__r = r

    def imprime_posicao(self):
        print( "(" + str(self.__x) + "," + str(self.__y) + ")" )

