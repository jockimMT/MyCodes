import random

def menu():
    print("*" * 30)
    print("1 - multiplicar")
    print("2 - Maior Linha")
    print("3 - Sair")
    print("*" * 30)


#cria uma matriz com valores aleatórios entre -10 e 10
# solicita ao usuário o número de linhas e colunas

def criarmatrizR():
    
    while True:
        try:
            linhas = int(input("Informe o número de linhas: "))
            colunas = int(input("Informe o número de colunas: "))
            break
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(random.randint(-10, 10))
        matriz.append(linha)
    return matriz


'''Cria uma matriz com valores iguais a um valor informado pelo usuário
   para auxiliar na multiplicação de matrizes'''
   
def criar_matriz(linhas, colunas, valor=0):
    matriz = []
    for _ in range(linhas):
        linha = []
        for _ in range(colunas):
            linha.append(valor)
        matriz.append(linha)
    return matriz


'''Imprime a matriz de forma formatada, com os valores separados por espaço'''

def imprimirMatriz(matriz):
    for linha in matriz:
        print(" ".join(str(x) for x in linha))


'''Encontra a linha com a maior soma de elementos e imprime essa soma e a linha correspondente'''

def maior_elemento(matriz):
    maior = 0
    maior_linha = 0
    soma = 0
    for linha in matriz:
        for valor in linha:
            soma  = soma + valor
        if soma > maior:
            maior = soma
            maior_linha = matriz.index(linha)
        soma = 0
    print("Soma da maior linha", maior, ", na linha:", matriz[maior_linha])


'''Multiplica duas matrizes, 
   verificando se o número de colunas da primeira matriz é igual ao número de linhas da segunda matriz.
   Retorna a matriz resultante ou None se as dimensões não forem compatíveis.'''
   
def multiplica_matrizes(m1, m2):
    linhas1 = len(m1)
    colunas1 = len(m1[0])
    colunas2 = len(m2[0])
    resultado = criar_matriz(linhas1, colunas2)
    n = ("O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz.")
    if len(m2) != colunas1:
        print("O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz.")
        return None
    else:
        for i in range(linhas1):
            for j in range(colunas2):
                soma = 0
                for k in range(colunas1):
                    soma += m1[i][k] * m2[k][j]
                resultado[i][j] = soma
        return resultado