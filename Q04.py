'''Faça um programa que grave uma lista com 15 posições, calcule e mostre:
a) O maior elemento da lista e em que posição esse elemento se encontra;
b) O menor elemento da lista e em que posição esse elemento se encontra.'''

from random import randint


def gravar_lista():
    lista = []
    for _ in range(15):  # O uso do _ é uma convenção em Python
        # para indicar uma variável que não será utilizada posteriormente no código.
        num = randint(-100, 100)  # variável recebe números aleatórios entre -100 e 100
        lista.append(num)  # esses números são adicionados à lista, antes vazia
    return lista


def maior_menor(lista):
    maior = lista[0]  # maior e menor recebem o primeiro valor da lista
    menor = lista[0]  # dessa forma os valores seguintes serão comparados a seguir
    posicao_maior = posicao_menor = 0
    for i in range(len(lista)):  # percorre o comprimento da lista
        if lista[i] >= maior:  # se o índice da lista for maior ou igual ao primeiro valor da lista
            maior = lista[i]  # maior recebe esse índice da lista
            posicao_maior = i + 1  # sua posição revelada pelo índice do for
        elif lista[i] <= menor:
            menor = lista[i]
            posicao_menor = i + 1
    return maior, posicao_maior, menor, posicao_menor


lista = gravar_lista()
maior, posicao_maior, menor, posicao_menor = maior_menor(lista)
print(f'Lista: {lista}')
print(f'Maior número: {maior}, sua posição {posicao_maior}')
print(f'Menor número: {menor}, sua posição {posicao_menor}')
