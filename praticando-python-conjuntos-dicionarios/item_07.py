# Recebe e trata as permissões principais
principais = input("Permissões principais: ").lower().split(",")
principais = set(perm.strip() for perm in principais)

# Recebe e trata as permissões solicitadas
solicitadas = input("Permissões solicitadas: ").lower().split(",")
solicitadas = set(perm.strip() for perm in solicitadas)

# Verificação de inclusão
if solicitadas.issubset(principais):
    print("\nAs permissões solicitadas fazem parte das permissões principais.")
else:
    print("\nAs permissões solicitadas não fazem parte das permissões principais.")
