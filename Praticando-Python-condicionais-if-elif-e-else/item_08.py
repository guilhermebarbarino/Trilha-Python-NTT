limite = 3000.00
despesas = float(input("Digite o total de despesas realizadas neste mês: R$ "))

if despesas > limite:
    print("Atenção: Você ultrapassou o limite de gastos!")
else:
    print("Parabéns! Você está dentro do seu orçamento.")
