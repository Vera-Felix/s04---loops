# Exercicio quadrado, teremos uma lista com alguns números e vamos gerar uma nova lista com o 
# quadrado desses números.

# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos
# quadrados dos elementos do vetor.

lista_numeros = [5, 4, 3, 6, 10, 12, 25, 80, 9, 21]

for item_lista in lista_numeros:
    quadrado = item_lista * item_lista
    print(quadrado)