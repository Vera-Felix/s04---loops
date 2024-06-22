# Exemplo 1: Dividir uma String em Palavras
# Cenário: Frase Simples

# Uma frase simples
frase = "Eu estou aprendendo Python"

# Dividindo a frase em palavras
frase = "Eu estou aprendendo Python"
palavras = frase.split()
print(palavras)  # Saída: ['Eu', 'estou', 'aprendendo', 'Python']

#Exemplo 2: Dividir uma String por Vírgula
# Cenário: Lista de Itens Separados por Vírgulas

# Uma lista de frutas separadas por vírgulas
frutas = "Maçã,Banana,Cereja,Uva"

# Dividindo a string em uma lista de frutas
frutas = "Maçã,Banana,Cereja,Uva"
lista_frutas = frutas.split(',')
print(lista_frutas)  # Saída: ['Maçã', 'Banana', 'Cereja', 'Uva']

# Exemplo 3: Dividir uma String por Espaços Múltiplos
# Cenário: String com Espaços Múltiplos

# Uma frase com múltiplos espaços
frase = "Python    é   uma   linguagem  poderosa"

# Dividindo a frase em palavras usando o delimitador de espaço padrão
frase = "Python    é   uma   linguagem  poderosa"
palavras = frase.split()
print(palavras)  # Saída: ['Python', 'é', 'uma', 'linguagem', 'poderosa']

# Exemplo 4: Dividir uma String por Caracteres Específicos
# Cenário: Data no Formato YYYY-MM-DD
# Uma data no formato YYYY-MM-DD
data = "2024-06-22"

# Dividindo a data em ano, mês e dia
data = "2024-06-22"
ano, mes, dia = data.split('-')
print(f"Ano: {ano}, Mês: {mes}, Dia: {dia}")
# Saída: Ano: 2024, Mês: 06, Dia: 22