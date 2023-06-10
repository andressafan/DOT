'''Faça um programa que dada uma seqüência de n números, imprimi-la na ordem inversa à da
leitura.'''

from random import randint


def gerar_lista():
    lista = []  # lista vazia
    while True:  # teste para verificar se o número é inteiro
        # se não for o programa retorna uma menssagem de erro e repete a entrada de um número 'n'
        try:
            n = int(input('Digite quantos números deseja dentro da lista: '))
            break  # Sai do loop se a conversão para inteiro foi bem-sucedida
        except ValueError:
            print('Valor inválido. Digite um número inteiro.')
    for num in range(n):  # loop que percorre 'n' ex:  n = 4
        num = randint(-100, 100)  # num recebe um valor aleatório entre -100 e 100 4 vezes: 2: 6: 55: -26
        lista.append(num)  # adiciona o valor à lista: [2, 6, 55, -26]
        # índices                                     [0, 1,  2,  3 ]
    return lista


def inverso(lista):  # função inverso chama parâmetro (lista) da função acima
    inverso = []  # cria uma nova lista vazia chamada inverso
    for i in range(len(lista) - 1, - 1, -1):  # loop em que o índice começa a percorrer
        # do comprimento da lista início (4 - 1) (3)
        # até o índice (-1), (-1) não é incluído ou seja vai até o índice (0)
        # será lido diminuindo 1 a cada iteração (-1)
        inverso.append(lista[i])  # adiciona a cada iteração o número à lista:
        # adiciona o valor do índice i da lista original à lista inverso.
    return inverso


lista = gerar_lista()  # função gerar_lista() armazenada na variável lista
inverso_lista = inverso(lista)  # função inverso(lista) armazenada na variável inverso_lista
print(f'Lista original: {lista}')
print(f'Lista invertida: {inverso_lista}')
