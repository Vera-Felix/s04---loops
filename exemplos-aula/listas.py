frutas = ["abacaxi"]
frutas.append("uva") # adiciona só um item
print(frutas)

frutas = ["laranja","uva"]
frutas.extend(["morango", "abacaxi"]) # adicona mais de um item
print(frutas)

frutas = ["laranja", "uva", "morango","abacate","cereja"]
frutas.extend(["pera","melão","banana"])
print(frutas)

# frutas[1] index - Print a fruta q está na posição 1.
# nesse caso é uva. Index começa na posição zero.
frutas = ["laranja", "uva", "morango","abacate","cereja"]
print(frutas[1])

# index - print a posição q está determinada frutas.
# Index começa na posição zero.
frutas = ["laranja", "uva", "morango","abacate","cereja"]
print(frutas.index("abacate"))

# sort - coloca em ordem alfabética
frutas = ["laranja", "uva", "morango","abacate","cereja"]
frutas.sort()
print(frutas)

# len - qtd de elementos dentro da variável
frutas = ["laranja", "uva", "morango","abacate","cereja"]
print(len(frutas))
print(frutas)

# pop- remove o último item
frutas = ["laranja", "uva", "morango","abacate","cereja"]
frutas.pop()
print(frutas)