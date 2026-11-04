from random import randint

def validador_cpf():    
    while True:
        try:
            cpf = input("Digite o CPF: ").replace('.', '').replace('-', '')
            cpfint = int(cpf)
            if cpf is None or len(cpf) != 11 or cpf == cpf[0] * len(cpf):
                raise ValueError("CPF deve ter 11 digitos diferentes.")
            break
        except ValueError:
            print("CPF invalido.")

    n = 0

    while n < 2:
        soma = 0
   
        if n == 0:
            for i in range(0,9):
                soma += int(cpf[i]) * (10 - i)

            mult = (soma * 10) % 11

            if mult > 9:
                digito1 = 0
            else:
                digito1 = (soma * 10) % 11 
        
            print(f'Digito 1: {digito1}')

        if n == 1:
            for i in range(0,10):
                soma += int(cpf[i]) * (11 - i)
            
            mult = (soma * 10) % 11

            if mult > 9:
                digito2 = 0
            else:
                digito2 = (soma * 10) % 11
        
            print(f'Digito 2: {digito2}')

        n += 1

    if digito1 != int(cpf[9]) or digito2 != int(cpf[10]):
        print("CPF invalido.")
    else:
        print("CPF valido.")
        print(f"CPF: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}")

def gerador_cpf():
    nove_digitos = ''.join([str(randint(0, 9)) for _ in range(9)])
    cpf = nove_digitos
    n = 0

    while n < 2:
        soma = 0
   
        if n == 0:
            for i in range(0,9):
                soma += int(cpf[i]) * (10 - i)

            mult = (soma * 10) % 11

            if mult > 9:
                digito1 = 0
            else:
                digito1 = (soma * 10) % 11 
        
            print(f'Digito 1: {digito1}')
            cpf += str(digito1)

        if n == 1:
            for i in range(0,10):
                soma += int(cpf[i]) * (11 - i)
            
            mult = (soma * 10) % 11

            if mult > 9:
                digito2 = 0
            else:
                digito2 = (soma * 10) % 11
        
            print(f'Digito 2: {digito2}')

        n += 1

    cpf += str(digito2)
    print("CPF gerado com sucesso.")
    print(f"CPF: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}")

def main():
    while True:
        print("1. Validar CPF")
        print("2. Gerar CPF")
        print("3. Sair")
        
        opcao = input("Escolha uma opcao: ")
        
        if opcao == '1':
            validador_cpf()
        elif opcao == '2':
            gerador_cpf()
        elif opcao == '3':
            break
        

main()

