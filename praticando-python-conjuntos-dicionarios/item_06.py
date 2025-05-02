# Recebe as listas e transforma tudo em letras minúsculas, separando pelos itens
lista_laura = input("Lista de Laura: ").lower().split(",")
lista_ana = input("Lista de Ana: ").lower().split(",")

# Remove espaços desnecessários em volta dos itens
itens_laura = set(item.strip() for item in lista_laura)
itens_ana = set(item.strip() for item in lista_ana)

# Itens em comum
itens_comuns = itens_laura & itens_ana

# Exclusivos de cada uma
exclusivos_laura = itens_laura - itens_ana
exclusivos_ana = itens_ana - itens_laura

# Exibindo os resultados
print("\nItens em ambas as listas:", ", ".join(sorted(itens_comuns)))
print("Itens exclusivos de Laura:", ", ".join(sorted(exclusivos_laura)))
print("Itens exclusivos de Ana:", ", ".join(sorted(exclusivos_ana)))
