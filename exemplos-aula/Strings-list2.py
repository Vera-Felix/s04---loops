# Exemplo 4: Filtrando uma Lista de Strings
# Cenário: Lista de Palavras

# Criando uma lista de palavras
palavras = ["gato", "cachorro", "elefante", "girafa", "leão"]

# Filtrando palavras que começam com a letra 'g'
palavras_com_g = [palavra for palavra in palavras if palavra.startswith('g')]
print(palavras_com_g)  # Saída: ['gato', 'girafa']

# Exemplo 5: Combinando e Dividindo Strings em Listas
# Cenário: Transformar uma String em Lista de Palavras e Vice-Versa
# Uma string de frutas
frutas_str = "Maçã, Banana, Cereja, Uva"

# Convertendo a string em uma lista de frutas
frutas_lista = frutas_str.split(", ")
print(frutas_lista)  # Saída: ['Maçã', 'Banana', 'Cereja', 'Uva']

# Combinando a lista de frutas em uma única string
frutas_str = "Maçã, Banana, Cereja, Uva"
frutas_lista = frutas_str.split(", ")
frutas_str_nova = ", ".join(frutas_lista)
print(frutas_str_nova)  # Saída: 'Maçã, Banana, Cereja, Uva'