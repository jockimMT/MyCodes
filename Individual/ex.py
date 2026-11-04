import os

lista = []

def menu():
    print("1. Inserir")
    print("2. Excluir")
    print("3. Listar")
    print("4. Sair")
    
     
def listar():
    print("Listando itens...")
    if not lista:
        print("A lista está vazia.")
    else:
        print("Itens na lista:")
        for i, item in enumerate(lista):
            print(i, item)

def inserir():
    print("Inserindo item...")
    item = input("Digite o item a ser inserido: ")
    if item in lista:
        print(f"Item '{item}' já existe na lista.")
        return
    if item:    
        lista.append(item)
        print(f"Item '{item}' inserido com sucesso.")
    
def excluir():
    print("Excluindo item...")
    if not lista:
        print("A lista está vazia. Não há itens para excluir.")
        return
    item = input("Digite o item a ser excluído: ")
    if item in lista:
        lista.remove(item)
        print(f"Item '{item}' excluído com sucesso.")
    else:
        print(f"Item '{item}' não encontrado na lista.")
        
    
def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        
        try:
            opcao = int(opcao)
            if opcao == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                inserir()
            elif opcao == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                excluir()
            elif opcao == 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                listar()
            elif opcao == 4:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Saindo do programa.")
                break
            else:
                print("Opção inválida. Por favor, escolha um número entre 1 e 4.")
        except ValueError:
            print("Opção inválida. Por favor, escolha um número entre 1 e 4.")
            continue

        
main()