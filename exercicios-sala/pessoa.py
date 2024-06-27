dicionario = {
    "nome": "Ana",
    "idade": 25
}

print(dicionario["nome"])

# adicionar cidade
dicionario["cidade"] = "São Paulo"
print(dicionario)

# verificar se "idade" tem no dicionario
print("idade" in dicionario)
print("estado" in dicionario)

# lista de dicionarios
dicionario_pessoa_2 = {
    "nome": "vera",
    "idade": 55
}
lista_dicionario = [dicionario, dicionario_pessoa_2]
print(lista_dicionario)

dicionario_pessoa_3 = {
    "nome": "Paulo"
}
idade = input("Digite sua idade: ")
dicionario_pessoa_3["idade"] = idade
print(dicionario_pessoa_3)