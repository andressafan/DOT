'''Faça um programa que leia duas listas de 10 elementos numéricos cada uma e intercale os
elementos deste em uma outra lista de 20 elementos.'''

from random import randint


def listas():
    lista1 = []
    lista2 = []
    for _ in range(10):  # loop de 10 voltas
        num1 = randint(-100, 100)  # num1 sorteia um número aleatório
        num2 = randint(-100, 100)  # num2 sorteia outro número aleatório
        lista1.append(num1)  # lista 1 recebe os sorteios da variável num1
        lista2.append(num2)  # lista 2 recebe os sorteios da variável num2
    return lista1, lista2


def intercalar(lista1, lista2):  # função recebe como parâmetros as duas listas geradas
    lista3 = []
    for i in range(10):  # loop de 10 voltas (iterações)
        lista3.append(lista1[i])  # a cada iteração a lista3 vai receber um índice da lista1
        lista3.append(lista2[i])  # e um índice da lista2
        # note que por adicionar dois elementos a cada iteração ao fim vai ter adicionado 20 elementos
    return lista3


lista1, lista2 = listas()
lista3 = intercalar(lista1, lista2)
print(f'Primeira lista: {lista1}')
print(f'Segunda lista: {lista2}')
print(f'Lista intercalada: {lista3}')
