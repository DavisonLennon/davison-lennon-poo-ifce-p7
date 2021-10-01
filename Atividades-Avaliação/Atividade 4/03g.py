# 03g.py: questao 3g

class Conta():
    def __init__(self, agencia, n_conta):
        self.__agencia = agencia
        self.__n_conta = n_conta

class ContaCorrente(Conta):
    def __init__(self, agencia, n_conta):
        super().__init__(agencia, n_conta)

class Cliente():
    def __init__(self, nome, agencia, n_conta):
        self.__conta_corrente = ContaCorrente(agencia, n_conta)
        self.__nome = nome


