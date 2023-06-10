'''Dada uma lista contendo 10 elementos numéricos, elabore um programa que verifique se um
outro valor dado pertence ou não à lista.'''

from random import randint


def gerar_lista():
    lista = []
    for _ in range(10):
        num = randint(-100, 100)
        lista.append(num)
    return lista


def verif(lista, num):  # função que verifica se o número está ou não na lista
    if num in lista:
        return f'O número {num} está dentro da lista.'
    else:
        return f'O número {num} não está na lista.'


def main():
    while True:  # loop parado pelo break
        try:  # recebe os valor de num digitado pelo usuário e chama a função gerar_lista() pra mostrar a lista
            # e chama a função verif() para fzr a verificação
            num = int(input('Digite um número: '))
            lista = gerar_lista()
            print(f'A lista é:')
            print(lista)
            print(f'Foi verificado que:')
            print(verif(lista, num))
            break  # se tudo ocorrer corretamente o loop é parado ao fim dos prints
        except ValueError:  # se ocorrer um caso de ValueError
            # ou seja se o valor inserido requisitado pelo input não for int a menssagem de erro será apresentada
            print('Erro: Digite um número inteiro válido.')


if __name__ == '__main__':
    main()
