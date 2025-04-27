import re

cpf = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")

if re.fullmatch(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
    print("O CPF está no formato correto.")
else:
    print("O CPF está no formato incorreto.")
