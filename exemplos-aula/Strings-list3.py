# Exemplo 6: Encontrando o Comprimento das Strings em uma Lista
# Cenário: Lista de Nomes

# Criando uma lista de nomes
nomes = ["Ana", "Bruno", "Carla", "Daniel"]

# Calculando o comprimento de cada nome
comprimentos = [len(nome) for nome in nomes]
print(comprimentos)  # Saída: [3, 5, 5, 6]