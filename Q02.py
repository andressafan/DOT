# 2) Faça um programa que grave uma lista com dez números reais, calcule e mostre a quantidade
# de números negativos e a soma dos números positivos dessa lista.

from random import randint


def gravar_lista():
    lista = []
    for num in range(10):
        num = randint(-100, 100)
        lista.append(num)
    return lista


def qnt(lista):
    qnt_negativo = soma_positivo = 0
    for num in lista:
        if num < 0:
            qnt_negativo += 1
        else:
            soma_positivo += num
    return qnt_negativo, soma_positivo


def main():
    lista = gravar_lista()
    qnt_negativo, soma_positivo = qnt(lista)

    print('Lista com 10 números reais:')
    print(lista)
    print('Quantidade de números negativos:')
    print(qnt_negativo)
    print('Soma dos números positivos:')
    print(soma_positivo)


if __name__ == '__main__':
    main()
