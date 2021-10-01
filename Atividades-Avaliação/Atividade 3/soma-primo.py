```# somaprimos.py: função que soma os n primeiros primos.
#

def primo(p):
    contador = 0
    for i in range(1, p + 1):
        if p % i == 0:
            contador = contador + 1
    if contador == 2:
        return True
    else:
        return False

def somaprimos(n):
    soma = 0
    conta_primos = 0
    i = 2

    if n >= 1:
        while conta_primos < n:
            if primo(i):
                soma = soma + i
                conta_primos = conta_primos + 1
            i = i + 1
    
    print(soma)```
