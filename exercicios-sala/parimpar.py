# Exercicio par ou impar, teremos uma lista com alguns números e vamos dividir em duas listas 
# uma com números pares e outra com números impares.

#Faça um Programa que leia 10 números inteiros e armazene-os num vetor. 
#Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_par = []
lista_impar = []

for numero in lista:
    if numero %2 == 0:
        lista_par.append(numero)    
    else:
        lista_impar.append(numero)

print("Lista original", lista)
print("Lista par", lista_par)
print("Lista_impar", lista_impar)