# 1) Faça um programa que grave uma lista de 100 elementos numéricos inteiros e:
# a) Mostre a quantidade de números pares;
# b) Grave uma lista somente com os números pares e mostre a lista;
# c) Mostre a quantidade de números ímpares;
# d) Grave uma lista somente com os números ímpares e mostre a lista.


# A função gravar_lista(qtd) recebe um número qtd como parâmetro
# e solicita ao usuário que digite um número qtd vezes.
# Cada número é verificado se é um inteiro válido e, em seguida,
# adicionado à lista lista usando o método append(). Caso o usuário
# digite um valor inválido, uma mensagem de erro é exibida e o usuário
# é solicitado a digitar novamente.
def gravar_lista(qtd):
    lista = []
    for _ in range(qtd):
        while True:
            try:
                numero = int(input("Digite um número: "))
                lista.append(numero)
                break
            except ValueError:
                print("Valor inválido. Digite novamente.")
    return lista

# A função contar_pares(lista) recebe a lista de números lista
# e inicializa uma variável qtd_pares como zero.
# Em seguida, percorre cada número na lista e verifica se é par
# (ou seja, se o resto da divisão por 2 é zero).
# Se for par, incrementa qtd_pares em 1. No final, retorna o valor de qtd_pares.
def contar_pares(lista):
    qtd_pares = 0
    for num in lista:
        if num % 2 == 0:
            qtd_pares += 1
    return qtd_pares

# A função filtrar_pares(lista) recebe a lista de números lista
# e inicializa uma lista vazia lista_pares.
# Percorre cada número na lista e verifica se é par.
# Se for par, adiciona o número à lista lista_pares.
# No final, retorna a lista lista_pares contendo apenas os números pares.

def filtrar_pares(lista):
    lista_pares = []
    for num in lista:
        if num % 2 == 0:
            lista_pares.append(num)
    return lista_pares


def contar_impares(lista):
    qtd_impares = 0
    for num in lista:
        if num % 2 != 0:
            qtd_impares += 1
    return qtd_impares


def filtrar_impares(lista):
    lista_impares = []
    for num in lista:
        if num % 2 != 0:
            lista_impares.append(num)
    return lista_impares

# Aqui são criadas variáveis para receber cada função
# e printadas na tela se é chamada cada variável

# Programa principal


lista_numeros = gravar_lista(10)

qtd_pares = contar_pares(lista_numeros)
lista_pares = filtrar_pares(lista_numeros)

qtd_impares = contar_impares(lista_numeros)
lista_impares = filtrar_impares(lista_numeros)

print("Quantidade de números pares:", qtd_pares)
print("Números pares:", lista_pares)
print("Quantidade de números ímpares:", qtd_impares)
print("Números ímpares:", lista_impares)