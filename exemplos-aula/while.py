# O comando while faz com que um conjunto de instruções 
# seja executado enquanto uma condição é atendida. 
# Quando o resultado dessa condição passa a ser falso, 
# a execução do loop é interrompida, 
# como mostra o exemplo a seguir:

contador = 0
while (contador < 5):
       print(contador)
       contador   = contador + 1

#Ao final do while podemos utilizar a instrução else. 
# O propósito disso é executar alguma instrução ou bloco de 
# código ao final do loop,
# como podemos ver no exemplo a seguir:

contador = 0
while (contador < 5):
      print(contador)
      contador = contador + 1
else:
      print("O loop while foi encerrado com sucesso!")

# No loop while, a expressão é testada enquanto for verdadeira. 
# A partir do momento que ela se torna falsa, 
# o código da cláusula else será executado, se estiver presente.

x = 0
while x < 10:
    print(x)
    x += 1
else:
    print("fim while")

# Se dentro da repetição for executado um break, 
# o loop será encerrado sem executar o conjunto da cláusula else.

x = 0
while x < 10:
    print(x)
    x += 1
    if x == 6:
        print("x é igual a 6")
        break
else:
    print("fim while")