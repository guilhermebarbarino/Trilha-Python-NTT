projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

for projeto in projetos:
    if projeto is not None:
        print(projeto)
    else:
        print("Projeto ausente")