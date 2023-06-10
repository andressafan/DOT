'''Dadas duas listas, uma contendo a quantidade e a outra o preço de 20 produtos, elabore um
programa que calcule e exiba o faturamento que é igual a quantidade x preço. Calcule e exiba
também o faturamento total que é o somatório de todos os faturamentos, a média dos faturamentos
e quantos faturamentos estão abaixo da média.'''


def criar_listas():  # Função que vai criar as listas
    qnt = []  # lista de quantidade de produtos vazia
    preco = []  # lista de preços de produtos vazia
    for i in range(20):  # aqui temos um lopp de 20 iterações
        while True:  # loop infinito que só acaba com um break ou condição de parada
            try:  # usada para lidar com exceções, executa o bloco dentro dele e se houver exceção é tratada com except
                quantidade = int(input(
                    f'Digite quantas unidades do {i + 1}° produto deseja: '))  # quantidade do produto adicionada
                # pelo usuário
                if quantidade < 0:  # se a quantidade for maior que zero
                    raise ValueError(
                        'A quantidadade deve ser um número positivo maior que zero!')  # retorna um valor de erro
                    # personalizada por raise
                    # (levanta um valor de erro personalizado)
                precos = float(input(f'Digite o preço do {i + 1}° produto: '))  # preço adicionado pelo usuário
                if precos < 0:  # se esse preço for menor que 0, então preço não é valido
                    raise ValueError('O preço deve ser um valor maior que zero!')  # retorna um valor de erro
                break  # após as verificações acima break para o programa
            except ValueError as e:  # Em caso de ocorrer um ValueError, o bloco except será executado e a variável
                # 'e' irá armazenar a exceção
                # e será exibida a mensagem de erro associada à exceção utilizando o formato Erro: {mensagem_de_erro}."
                print(f'Erro: {e}')
        qnt.append(quantidade)
        preco.append(precos)
    return qnt, preco


def cal_valores(qnt, preco):  # essa função irá calcular
    # lista de faturamentos
    # somatório de todos os faturamentos
    # média dos faturamentos
    # quantos faturamentos abaixo da média
    lista_fat = []
    som = qnt_m = 0
    for i in range(len(qnt)):  # loop que passa pelos comprimento da lista qnt: qnt = [2, 4, 5, 7, 8]
                                                                                   #  [0, 1, 2, 3, 4]
        valor = preco[i]  # valor vai ser igual aos índices da lista preço
        fat = qnt[i] * valor  # fat vai ser igual aos índices da lista qnt vezes os índices da lista valor
        lista_fat.append(fat)  # adiciona-se à lista os respectivos faturamentos
        som += fat  # somatorio vai somar cada fat
    media = som / len(qnt)  # media é igual ao total de somatório dividido pelo comprimento da lista qnt
    for i in lista_fat:  # outro loop q percorre os valores da lista_fat
        if i < media:  # se o valore for menor que a media
            qnt_m += 1  # adiciona mais 1 à quantidade de valores abaixo da média
    return lista_fat, som, media, qnt_m


def main():
    qnt, preco = criar_listas()
    lista_fat, som, media, qnt_m = cal_valores(qnt, preco)
    print('Respectivamente')
    print(f'Lista com as quantidades dos produtos:')
    print(qnt)
    print('Lista com os preços dos produtos:')
    print(preco)
    print('Lista com os valores de faturamento de cada produto')
    print(lista_fat)
    print(f'Somatório dos faturamentos: {som}')
    print(f'Média dos faturamentos: {media}')
    print(f'Quantidade de faturamentos abaixo da média: {qnt_m}')


if __name__ == "__main__":
    main()
