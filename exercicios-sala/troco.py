# Gerador de trocos
# Iremos criar um gerador de trocos:
# O cliente compra um produto que tem um valor X
# O cliente paga com uma nota de valor Y
# Nós teremos uma quantidade de notas no nosso caixa 
# e iremos ver quantas notas de cada uma iremos entregar para o cliente, para formar o troco.
# *A quantidade de notas já está definida no exercício.

    #O dicionário estará sempre ordenado das notas maiores para as menores
notas = {
        50: 3,
        10: 5,
        5: 7,
        1: 3
    }

#Utilizar valores inteiros, não temos centavos
valor_produto = int(input("Digite o valor do produto: "))
valor_pago = int(input("Digite o valor que foi pago: "))

if valor_pago < valor_produto:
    print("Valor pago é insuficiente")
else:
    troco = valor_pago - valor_produto
    