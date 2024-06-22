# (' '): espaço como separador
frase = "Vera bonita"
palavras = frase.split(' ')
print(palavras)
# resultado ['Vera', 'bonita']

# (','): vírgula como separador
dados = "Nome, Idade, Cidade"
colunas = dados.split(',')
print(colunas)
# resultado ['Nome', ' Idade', ' Cidade']

#('.'): ponto como separador
numero = "1.2.3"
numeros = numero.split('.')
print(numeros)

# (';'): ponto e vírgula como separador
frutas = "abacaxi;uva;banana"
lista_frutas = frutas.split(';')
print(lista_frutas)
# resultado ['abacaxi', 'uva', 'banana']

# ('\n'): quebra de Linha como separador
texto = "Linha 1\nLinha 2\nLinha 3"
linhas = texto.split('\n')
print(linhas)
# Resultado: ['Linha 1', 'Linha 2', 'Linha 3']

# (' '): Outros Caracteres Específicos como separador
frase = "Python;é;uma;linguagem;versátil"
palavras = frase.split(';')
print(palavras)
# Resultado: ['Python', 'é', 'uma', 'linguagem', 'versátil']