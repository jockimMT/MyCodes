import re
import os

arquivo = "conversa.txt"

usuario1 = input("Digite o nome do primeiro usuário: ")
usuario2 = input("Digite o nome do segundo usuário: ")

if not os.path.exists(arquivo):
    print(f"O arquivo {arquivo} não foi encontrado.")
    exit(1)

padrão = re.compile(
    r'(\d{2}/\d{2}/\d{4} \d{2}:\d{2} - (.*?)',
    re.MULTILINE
    )

with open(arquivo, 'r', encoding='utf-8') as file:
    conteudo = file.read()

mensagens = padrão.findall(conteudo)
total_mensagens = len(mensagens)


cont_usuario1 = sum(1 for m in mensagens if usuario1 in m)
cont_usuario2 = sum(1 for m in mensagens if usuario2 in m)

cont_outros = total_mensagens - cont_usuario1 - cont_usuario2

dias = input("Digite o número de dias para a análise: ")

if dias.isdigit():
    dias = int(dias)

    média_total = total_mensagens / dias
    media_u1 = cont_usuario1 / dias
    media_u2 = cont_usuario2 / dias

else:
    dias = None
    media_total = None

print(f"📊Total de mensagens: {total_mensagens}")
print(f"🧍‍♂️Mensagens de {usuario1}: {cont_usuario1}")
print(f"🧍‍♂️Mensagens de {usuario2}: {cont_usuario2}")

if cont_outros > 0:
    print(f"⚙️Mensagens de sistema ou outros usuários: {cont_outros}")

if dias:
    print(f"🗓️Média diária total: {média_total:.2f}")
    print(f"🗓️Média diária de {usuario1}: {media_u1:.2f}")
    print(f"🗓️Média diária de {usuario2}: {media_u2:.2f}")


