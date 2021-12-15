"""
    Módulo notafiscal -
    Classe NotaFiscal - 
        Atributos :
            id        - informado.
            codigo    - informado.
            data      - informado.
            cliente   - informado.
            items     - informado
            valornota - calculado. 
"""
import datetime
from cliente        import Cliente
from produto        import Produto
from itemnotafiscal import ItemNotaFiscal


class NotaFiscal():         
    def __init__(self, Id, codigo, cliente):
        self._Id = Id
        self._codigo=codigo
        self._cliente=cliente 
        self._data=datetime.datetime.now()   
        self._itens=[]
        self._valorNota=0.0        
        
    def setCliente(self, cliente):
        if isinstance(cliente, Cliente):
            self._cliente=cliente    
            
    def adicionarItem(self, item): 
        if isinstance(item, ItemNotaFiscal):
            self._itens.append(item)
        
    def calcularNotaFiscal(self):
        valor=0.0
        for item in self._itens:
            valor = valor + item._valorItem
        self.valorNota=valor
     
    def imprimirNotaFiscal(self):       
        print(f"{'-':-^95}")
        print(f"NOTA FISCAL {self._data.strftime('%d/%m/%Y'):>83}")
        print(f"Cliente: {self._cliente._codigo} Nome: {self._cliente._nome}")
        print(f"CPF/CNPJ: {self._cliente._cnpjcpf}")
        print(f"{'-':-^95}")
        print(f"ITENS")
        print(f"{'-':-^95}")
        print(f"Seq   Descrição                                      QTD       Valor Unit           Preço")
        print("----  ---------------------------------------       -----     ------------     ----------------")

        for item in self._itens:
            print(f"{item._sequencial:0>3}   {item._descricao: <48} {item._quantidade: <14} {format(item._valorUnitario, '.2f'): <19} {format(item._valorItem, '.2f')}")

        print(f"{'_':_^95}")
        print(f"Valor total: {self.valorNota:.2f}")

