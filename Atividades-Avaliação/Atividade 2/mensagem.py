# mensagem.py: codifica uma mensagem para uma sequência de números
#

maior_palavra = ""

while True:
    mensagem = input()

    if mensagem != "0":
        palavras = mensagem.split()
        saida = ""
        i = 1

        for palavra in palavras:
            n_letras = len(palavra)

            if n_letras >= len(maior_palavra):
                maior_palavra = palavra
    
            if len(palavras) == 1:
                saida = str(n_letras)
            else:
                if i == len(palavras):
                    saida = saida + str(n_letras)
                else:
                    saida = saida + str(n_letras) + "-" 
            i = i + 1

        print(saida)
    else:
        print(maior_palavra)
        break

