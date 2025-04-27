while True:
    nome_usuario = input("Digite o nome de usuário (mínimo 5 caracteres): ")
    senha = input("Digite a senha (mínimo 8 caracteres): ")
    
    if len(nome_usuario) >= 5 and len(senha) >= 8:
        print("Cadastro realizado com sucesso!")
        break
    else:
        print("Nome de usuário ou senha inválidos. Tente novamente.\n")
