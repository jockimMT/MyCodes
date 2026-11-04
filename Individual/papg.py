D = input("Deseja calcular PA ou PG: ")

R = float(input("Qual a razão: "))
A1 = float(input("Qual o primeiro valor: "))
N = int(input("Quantos valores tem: "))
a = 0

while a < N:
    if D == "PA":
        print(A1, " ")
        A1 = A1 + R
        a = a + 1
    
    elif D == "PG":
        print(A1, " ")
        A1 = A1 * R
        a = a + 1