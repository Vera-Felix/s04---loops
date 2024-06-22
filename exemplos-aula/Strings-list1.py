# Exemplo 2: Iterando sobre uma Lista de Strings
# Cenário: Lista de Frutas

# Criando uma lista de frutas
frutas = ["Maçã", "Banana", "Cereja"]

# Iterando sobre a lista e imprimindo cada fruta
for fruta in frutas:
    print(fruta)

# Saída:
# Maçã
# Banana
# Cereja

# Exemplo 3: Ordenando uma Lista de Strings
# Cenário: Lista de Cidades
# Criando uma lista de cidades
cidades = ["São Paulo", "Rio de Janeiro", "Curitiba", "Belo Horizonte"]

# Ordenando a lista de cidades em ordem alfabética
cidades = ["São Paulo", "Rio de Janeiro", "Curitiba", "Belo Horizonte"]
cidades.sort()
print(cidades)  # Saída: ['Belo Horizonte', 'Curitiba', 'Rio de Janeiro', 'São Paulo']

# Ordenando a lista de cidades em ordem alfabética reversa
cidades = ["São Paulo", "Rio de Janeiro", "Curitiba", "Belo Horizonte"]
cidades.sort(reverse=True)
print(cidades)  # Saída: ['São Paulo', 'Rio de Janeiro', 'Curitiba', 'Belo Horizonte']