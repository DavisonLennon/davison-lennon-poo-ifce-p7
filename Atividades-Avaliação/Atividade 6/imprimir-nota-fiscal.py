def imprimirNotaFiscal(self):    
    print(f"{'-':-^95}") # Linha
    print(f"NOTA FISCAL {self._data.strftime('%d/%m/%Y'):>83}")
    print(f"Cliente: {self._cliente._codigo} Nome: {self._cliente._nome}")
    print(f"CPF/CNPJ: {self._cliente._cnpjcpf}")
    print(f"{'-':-^95}") # Linha
    print(f"ITENS")
    print(f"{'-':-^95}") # Linha
    print(f"Seq   Descrição                                      QTD       Valor Unit           Preço")
    print("----  ---------------------------------------       -----     ------------     ----------------")

    for item in self._itens:
        print(f"{item._sequencial:0>3}   {item._descricao: <48} {item._quantidade: <14} {format(item._valorUnitario, '.2f'): <19} {format(item._valorItem, '.2f')}")
    print(f"{'_':_^95}") # linha
    print(f"Valor total: {self.valorNota:.2f}")
