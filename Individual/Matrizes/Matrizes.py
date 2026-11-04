from biblioteca import *

# Criação de matrizes
print("Criar matriz A:")
matrizA = criarmatrizR()
print("Matriz A:")
imprimirMatriz(matrizA)

print("Criar matriz B:")
matrizB = criarmatrizR()
print("Matriz B:")
imprimirMatriz(matrizB)

#programa principal
while True:
    menu()
    
    #Solicita ao usuário uma opção
    #Error handling para garantir que a entrada seja um número inteiro
    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Opção inválida. Por favor, insira um número inteiro.")
        continue
    
    # Verifica a opção escolhida pelo usuário
    if opcao == 1:
        matrizC = multiplica_matrizes(matrizA, matrizB)
        if matrizC != None:
            print("Matriz C (resultado da multiplicação):")
            imprimirMatriz(matrizC)
    elif opcao == 2:
        print("Soma da maior linha de cada matriz:")
        print("Matriz A:")
        maior_elemento(matrizA)
        print("Matriz B:")
        maior_elemento(matrizB)
    elif opcao == 3:
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

