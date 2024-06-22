#Cenário: Lista de Tarefas
# Imagine que você está criando uma aplicação simples de lista de tarefas (to-do list). 
# Você pode usar uma lista para armazenar as tarefas.

# Criando uma lista de tarefas
tarefas = ["Comprar leite", "Estudar Python", "Limpar a casa"]
print(tarefas)

# Adicionar uma nova tarefa
tarefas = ["Comprar leite", "Estudar Python", "Limpar a casa"]
tarefas.append("Ir à academia")
print(tarefas)

# Remover uma tarefa concluída
tarefas = ["Comprar leite", "Estudar Python", "Limpar a casa"]
tarefas.remove("Comprar leite")
print(tarefas)

# Modificar uma tarefa
tarefas = ["Comprar leite", "Estudar Python", "Limpar a casa"]
tarefas[1] = "Estudar Python por 2 horas"
print(tarefas)

# Iterar sobre as tarefas e imprimir cada uma
tarefas = ["Estudar Python por 2h", "Limpar a casa","Ir à academia"]
for tarefa in tarefas:
    print(tarefa)
