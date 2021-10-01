# 03b.py: questão 3b

class Ponto():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property.setter
    def x(self, x):
        raise ValueError("Não eh possivel alterar o valor da propriedade 'x'.
                Utilize a funcao 'setx()'.")

    @property
    def y(self):
        return self.__y

    @property.setter
    def y(self, y):
        raise ValueError("Não eh possivel alterar o valor da propriedade 'y'.
                Utilize a funcao 'sety()'.")

    def setx(self, x):
        self.__x = x

    def sety(self, y):
        self.__y = y

