# Exemplo 1: Criando e Modificando uma Lista de Strings
# Cenário: Lista de Amigos

# Criando uma lista de amigos
amigos = ["Alice", "Bob", "Carlos"]
print(amigos)

# Adicionando um novo amigo à lista
amigos = ["Alice", "Bob", "Carlos"]
amigos.append("Diana")
print(amigos)  # Saída: ['Alice', 'Bob', 'Carlos', 'Diana']

# Removendo um amigo da lista
amigos = ["Alice", "Bob", "Carlos","Diana"]
amigos.remove("Bob")
print(amigos)  # Saída: ['Alice', 'Carlos', 'Diana']

# Modificando o nome de um amigo
amigos = ["Alice", "Bob", "Carlos","Diana"]
amigos[1] = "Carla" # remove o amigo q tá na posição ou índice 1
print(amigos)  # Saída: ['Alice', 'Carla', 'Diana']