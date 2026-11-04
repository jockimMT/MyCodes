from random_word import RandomWords
palavra = RandomWords().get_random_word()
palavra_oculta = ["_" for _ in palavra]
m = 0

def exibir_forca(n):
    if n == 0:
        print("      O      \n"
              "             \n"
              "             \n")
    elif n == 1:
        print("      O      \n"
              "      |     \n"
              "             \n")
    elif n == 2:
        print("      O      \n"
              "     /|      \n"
              "             \n")
    elif n == 3:
        print("      O      \n"
              "     /|\     \n"
              "             \n")
    elif n == 4:
        print("      O      \n"
              "     /|\     \n"
              "     /      \n")
    elif n == 5:
        print("      O      \n"
              "     /|\     \n"
              "     / \     \n")
       

while True:
    tentativa = input("Digite uma letra:").lower()
    if len(tentativa) != 1 or not tentativa.isalpha():
        print("Por favor, digite apenas uma letra.")
        continue
    
    if tentativa in palavra:
        for i, letra in enumerate(palavra):
            if letra == tentativa:
                palavra_oculta[i] = tentativa
        print("Boa! A palavra agora é:", " ".join(palavra_oculta).strip())
        
    if tentativa not in palavra:
        exibir_forca(m)
        m += 1
        print(f"Ops! A letra {tentativa} não está na palavra.")
        
    if m >= 6:
        print("Você perdeu! A palavra era:", palavra)
        break
        
    if "_" not in palavra_oculta:
        print("Parabéns! Você adivinhou a palavra:", palavra)
        break
    
