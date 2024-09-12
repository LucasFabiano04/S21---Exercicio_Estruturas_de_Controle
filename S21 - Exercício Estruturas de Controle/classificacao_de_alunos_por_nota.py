# Inicializa uma lista para armazenar os nomes e notas dos alunos
alunos = []
notas = []

# Inicializa a variável para somar as notas
soma_notas = 0

# Repetição para coletar dados de 5 alunos
for i in range(5):
    # Solicita o nome do aluno
    nome = input(f"Digite o nome do aluno {i+1}: ")
    
    # Solicita a nota do aluno
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    
    # Adiciona o nome e a nota às listas
    alunos.append(nome)
    notas.append(nota)
    
    # Adiciona a nota à soma total das notas
    soma_notas += nota

# Calcula a média da turma
media_turma = soma_notas / 5

# Exibe a média da turma
print(f"\nA média da turma é: {media_turma:.2f}")

# Repetição para classificar cada aluno
for i in range(5):
    # Verifica se a nota do aluno é maior ou igual a 7
    if notas[i] >= 7:
        # Se a nota for maior ou igual a 7, o aluno está aprovado
        status = "Aprovado"
    else:
        # Caso contrário, o aluno está reprovado
        status = "Reprovado"
    
    # Exibe o nome, a nota e o status do aluno
    print(f"{alunos[i]} - Nota: {notas[i]:.2f} - Status: {status}")