# Vamos ver um exemplo simples de como usar o 
# loop for para imprimir todos os números de 0 a 4.
# Note que a função range(5) cria uma sequência de 
# números de 0 a 4, 
# que é então iterada pelo loop for.

for i in range(5):
 print(i)

# Uma das aplicações mais comuns para o loop for 
# em Python é iterar através dos elementos de uma lista.

frutas = ['maçã', 'banana', 'cereja', 'kiwi', 'manga']

# Para imprimir cada elemento dessa lista, 
# podemos usar o seguinte loop for:

for fruta in frutas:
 print(fruta)

# As strings em Python são sequências imutáveis de caracteres.
# Utilizando o loop for, podemos percorrer cada caractere de uma 
# string de forma simples e intuitiva. 
# Vejamos um exemplo prático:

for char in "Python":
 print(char)

# Uma das funções mais poderosas 
# para controlar o loop for é o range(). 
# Com ele, podemos definir exatamente quantas vezes o loop 
# deve executar, 
# fornecendo um controle preciso sobre as nossas iterações.
# Por exemplo, se quisermos imprimir os números de 0 a 9, 
# podemos fazer da seguinte forma:

for i in range(10):
 print(i)

for i in range(1,10,2):
 print(i)

# Dicas e Truques: Break, Continue e Else no Loop for
# Para ter um controle ainda maior sobre a execução dos loops, 
# Python nos oferece as palavras-chave break, continue e else. 
# Cada uma dessas palavras-chave tem um propósito específico que 
# pode enriquecer a lógica dos nossos programas.

# Break: Utilizado para interromper imediatamente o loop, independentemente de sua condição de término.
# Continue: Pula a iteração atual e continua com a próxima iteração do loop.
# Else: Executado somente quando o loop for concluído sem interrupções pelo break.

# Veja como podemos utilizar o break e o else em um exemplo prático:

for num in range(1, 11):
# 1 é o valor inicial
# 11 é o valor final, a sequencia vai até 10
 print(num)
 if num == 5:
  break
else:
#O bloco else associado ao for só é executado se o loop não for interrompido por um break.
 print("Loop concluído com sucesso!")

# exemplo de range com 3 argumentos:
for num in range(2, 21, 3):
    print(num)

# Para ilustrar o uso completo com uma interrupção (break) e um bloco else:
for num in range(2, 21, 3):
    print(num)
    if num == 11:
        break
else:
    print("Loop concluído com sucesso!")

