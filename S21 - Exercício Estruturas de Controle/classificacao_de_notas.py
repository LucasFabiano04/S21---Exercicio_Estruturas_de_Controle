# Função principal para classificação das notas dos alunos
def classificacao_notas():
    while True:  # Inicia um laço de repetição para permitir a inserção de notas de vários alunos
        # Solicita a quantidade de notas que o usuário deseja inserir para um aluno
        quantidade_notas = int(input("Quantas notas deseja inserir para o aluno? "))
        
        soma_notas = 0  # Inicializa a variável para armazenar a soma das notas
        for i in range(quantidade_notas):  # Laço para inserir cada nota
            try:
                # Solicita a nota e a converte para um número decimal
                nota = float(input(f"Digite a nota {i + 1}: "))
                soma_notas += nota  # Adiciona a nota à soma das notas
            except ValueError:
                print("Nota inválida! Por favor, insira um número válido.")  # Captura erro se a entrada não for um número
                return  # Termina a função se houver uma entrada inválida
        
        # Calcula a média das notas
        media = soma_notas / quantidade_notas

        # Exibe a média das notas
        print(f"A média das notas é: {media:.2f}")

        # Estrutura de decisão composta para classificar o aluno com base na média
        if media >= 7.0:  # Se a média for maior ou igual a 7.0
            print("Status: Aprovado")  # Exibe que o aluno foi aprovado
        elif 5.0 <= media < 7.0:  # Se a média estiver entre 5.0 e 6.9
            print("Status: Recuperação")  # Exibe que o aluno está em recuperação
        else:  # Se a média for menor que 5.0
            print("Status: Reprovado")  # Exibe que o aluno foi reprovado

        # Pergunta ao usuário se deseja continuar inserindo notas
        continuar = input("Deseja inserir notas para outro aluno? (s/n): ")
        if continuar.lower() != 's':  # Se a resposta for diferente de 's' (sim)
            break  # Sai do laço e encerra o programa

# Chama a função para iniciar o programa
classificacao_notas()
