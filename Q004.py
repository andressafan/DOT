'''Faça um programa que grave uma lista com 15 posições, calcule e mostre:
a) O maior elemento da lista e em que posição esse elemento se encontra;
b) O menor elemento da lista e em que posição esse elemento se encontra.'''

from random import randint


def gravar_lista():
    lista = []
    for _ in range(15):  # O uso do _ é uma convenção em Python
        # para indicar uma variável que não será utilizada posteriormente no código.
        num = randint(-100, 100)  # a variável num recebe um número aleatório
        # entre -100 e 100
        lista.append(num)  # a cada iteração é adicionado o número sorteado
    return lista


def maior_menor(lista):
    maior = float('-inf')  # aqui nós estamos dizendo que a variávem maior tem um valor -infinito ou seja um valor
    # muito baixo
    # ou seja se o maior for um número infinitamente pequeno, qualquer número é maior que ele
    menor = float('+inf')  # aqui nós estamos dizendo que a variávem menor tem um valor +infinito ou seja um valor
    # muito baixo
    # ou seja se o menor for um número infinitamente grande, qualquer número é menor que ele
    posicao_maior = posicao_menor = 0  # aqui são criadas duas variável com posição do maior e posição do menor número

    for i, num in enumerate(lista):  # esse loop percorre a lista ultilizando enumerate
        # enumerate é uma função que retorna tanto o índice quanto o valor correspondente de cada elemento da sequência
        # i é o índice (localização interna na lista)
        # num seria os valores dentro da lista
        if num > maior:  # verifica se o numero na lista é maior que -infinito
            maior = num
            posicao_maior = i + 1
        if num < menor:  # verifica se o número na lista é menor que +infinito
            menor = num
            posicao_menor = i + 1  # retorna a posição interna na lista e adiciona 1
            # para que a contagem fique em ordem compreensivel (começando por 1 e não por 0)

    return maior, posicao_maior, menor, posicao_menor


lista = gravar_lista()
maior, posicao_maior, menor, posicao_menor = maior_menor(lista)

print(f"A lista gerada é: {lista}")
print(f"O maior elemento é {maior} e está na posição {posicao_maior}")
print(f"O menor elemento é {menor} e está na posição {posicao_menor}")
