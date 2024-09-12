# Programa para classificar pessoas por faixa etária

# Início do loop principal do programa
while True:
    # Solicita a entrada da idade do usuário
    idade = input("Digite a idade da pessoa (ou 'sair' para encerrar): ")
    
    # Verifica se o usuário deseja sair do programa
    if idade.lower() == 'sair':
        print("Programa encerrado.")
        break  # Encerra o loop e o programa

    # Tenta converter a entrada para um número inteiro
    try:
        idade = int(idade)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro ou 'sair'.")
        continue  # Retorna ao início do loop para nova entrada

    # Estrutura de decisão para classificar a idade
    if idade < 0:
        print("Idade não pode ser negativa.")
    elif idade < 18:
        print("A pessoa é menor de idade.")
    elif idade < 60:
        print("A pessoa é adulta.")
    else:
        print("A pessoa é idosa.")