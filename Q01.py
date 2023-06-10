"""1) Faça um programa em python que tenha:
a) Uma função para criar/gravar uma lista com 100 elementos numéricos inteiros; ok
b) Uma função para mostrar a quantidade de números pares e números ímpares;
c) Uma função para gerar duas outras listas, uma lista somente com os números
   pares da lista original e outra lista somente com os números ímpares;
d) Função para mostrar o maior elemento da lista original;
e) Mostrar as 3 listas no programa principal.  """

from random import randint

def criar_lista():
    lista = []
    for _ in range(100):
        num = randint(-100, 100)
        lista.append(num)
    return lista

def contar_pares_impares(lista):
    qtd_pares = 0
    qtd_impares = 0
    for num in lista:
        if num % 2 == 0:
            qtd_pares += 1
        else:
            qtd_impares += 1
    return qtd_pares, qtd_impares

def gerar_listas_pares_impares(lista):
    lista_pares = []
    lista_impares = []
    for num in lista:
        if num % 2 == 0:
            lista_pares.append(num)
        else:
            lista_impares.append(num)
    return lista_pares, lista_impares

def encontrar_maior_elemento(lista):
    maior = float('-inf')
    for num in lista:
        if num > maior:
            maior = num
    return maior

def main():
    lista = criar_lista()
    qtd_pares, qtd_impares = contar_pares_impares(lista)
    lista_pares, lista_impares = gerar_listas_pares_impares(lista)
    maior = encontrar_maior_elemento(lista)

    print(f'a) Lista original com os 100 números: {lista}')
    print(f'b) Quantidade de números pares: {qtd_pares}')
    print(f'   Quantidade de números ímpares: {qtd_impares}')
    print(f'c) Lista apenas com números pares: {lista_pares}')
    print(f'   Lista apenas com números ímpares: {lista_impares}')
    print(f'd) Maior elemento da lista original: {maior}')


if __name__ == '__main__':
    main()
