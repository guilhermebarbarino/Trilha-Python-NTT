temperatura = float(input("Digite a temperatura atual da sala de servidores (em °C): "))

if temperatura > 25:
    print("Alerta: Temperatura acima do permitido! Verifique o sistema de refrigeração.")
else:
    print("Temperatura dentro dos limites normais.")
