# 03a.py: questão 3a

class Ponto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circulo(Ponto):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r


