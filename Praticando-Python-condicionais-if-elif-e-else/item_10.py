nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"Média final: {media:.2f}")

if media >= 7:
    print("Aluno aprovado!")
elif 5 <= media < 7:
    print("Aluno em recuperação.")
else:
    print("Aluno reprovado.")
