# exemplos de dicionário:
pessoa = {
    "nome": "Paulo",
    "idade": 29,
    "filhos": [
        {"nome": "João", "idade": 6}, 
        {"nome": "Maria", "idade": 9}
    ]
}
print(pessoa)

capitais = {"Brasil": "Brasília", "Alemanha": "Berlim", "Japão": "Tóquio"}
capital_brasil = capitais["Brasil"]
print(capital_brasil)
print(capitais)

#Exemplo 1: Criando e acessando valores em um dicionário
# Criando um dicionário com informações de uma pessoa
pessoa = {
    'nome': 'Alice',
    'idade': 30,
    'cidade': 'São Paulo'
}

# Acessando valores no dicionário
print(pessoa['nome'])  # Saída: Alice
print(pessoa['idade'])  # Saída: 30
print(pessoa['cidade'])  # Saída: São Paulo

# Exemplo 2: Adicionando e atualizando valores em um dicionário
# Adicionando um novo par chave-valor
pessoa['profissao'] = 'Engenheira'

# Atualizando o valor de uma chave existente
pessoa['cidade'] = 'Rio de Janeiro'

print(pessoa)
# Saída: {'nome': 'Alice', 'idade': 30, 'cidade': 'Rio de Janeiro', 'profissao': 'Engenheira'}

 
# Exemplo 3: Iterando sobre um dicionário

# Iterando sobre as chaves do dicionário:
pessoa = {
    'nome': 'Alice',
    'idade': 30,
    'cidade': 'Rio de Janeiro',
    'profissão': 'engenheira'
    }

for chave in pessoa:
    print(chave, pessoa[chave])

# Saída:
# nome Alice
# idade 30
# cidade Rio de Janeiro
# profissao Engenheira

# for chave in pessoa::
# Este comando diz ao Python para pegar cada chave (por exemplo, 'nome', 'idade', etc.) 
# do dicionário pessoa, uma de cada vez.
# A cada iteração do loop, a variável chave terá um valor diferente que é uma chave do dicionário.
# print(chave, pessoa[chave]): chave é a chave atual do dicionário (por exemplo, 'nome').
# pessoa[chave] é o valor associado a essa chave no dicionário (por exemplo, 'Alice' para a chave 'nome').

# Iterando sobre os pares chave-valor:
pessoa = {
    'nome': 'Alice',
    'idade': 30,
    'cidade': 'Rio de Janeiro',
    'profissão': 'engenheira'
    }
for chave, valor in pessoa.items():
    print(chave, valor)

# Saída:
# nome Alice
# idade 30
# cidade Rio de Janeiro
# profissao Engenheira

# Exemplo 4: Usando o método get para acessar valores

# Usando o método get para acessar valores de forma segura
pessoa = {
    'nome': 'Alice',
    'idade': 30,
    'pais': 'Brasil',
    'profissão': 'engenheira'
    }
nome = pessoa.get('nome')  # Saída: Alice
pais = pessoa.get('pais', 'Brasil')  # Saída: Brasil (valor padrão)

print(nome)
print(pais)

# Exemplo 5: Removendo itens de um dicionário
pessoa = {
    'nome': 'Alice',
    'idade': 30,
    'pais': 'Brasil',
    'profissão': 'engenheira'
    }
# Removendo um item específico
idade = pessoa.pop('idade')
print(idade)  # Saída: 30

# Removendo o último item inserido
ultimo_item = pessoa.popitem()
print(ultimo_item)  # Saída: ('profissao', 'Engenheira')

# Exemplo 6: Dicionários aninhados
# Criando um dicionário aninhado
alunos = {
    'aluno1': {
        'nome': 'Carlos',
        'idade': 20
    },
    'aluno2': {
        'nome': 'Mariana',
        'idade': 22
    }
}

# Acessando valores em um dicionário aninhado
print(alunos['aluno1']['nome'])  # Saída: Carlos
print(alunos['aluno2']['idade'])  # Saída: 22