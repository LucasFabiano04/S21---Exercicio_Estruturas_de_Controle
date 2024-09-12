# Função principal que executa a calculadora
def calculadora():
    # Exibe as opções de operação para o usuário
    print("Escolha a operação desejada:")
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    
    # Solicita que o usuário escolha a operação (como string) e armazena na variável 'operacao'
    operacao = input("Digite o número correspondente à operação (1/2/3/4): ")

    # Solicita os dois números que o usuário deseja usar na operação
    try:
        num1 = float(input("Digite o primeiro número: "))  # Converte a entrada para número decimal
        num2 = float(input("Digite o segundo número: "))   # Converte a entrada para número decimal
    except ValueError:
        print("Entrada inválida! Por favor, insira números válidos.")  # Captura erro se entrada não for número
        return  # Termina a função se a entrada for inválida

    # Estrutura de decisão composta para verificar qual operação foi escolhida
    if operacao == '1':  # Se a operação for adição
        resultado = num1 + num2  # Realiza a adição
        print(f"O resultado de {num1} + {num2} é: {resultado}")  # Exibe o resultado
    elif operacao == '2':  # Se a operação for subtração
        resultado = num1 - num2  # Realiza a subtração
        print(f"O resultado de {num1} - {num2} é: {resultado}")  # Exibe o resultado
    elif operacao == '3':  # Se a operação for multiplicação
        resultado = num1 * num2  # Realiza a multiplicação
        print(f"O resultado de {num1} * {num2} é: {resultado}")  # Exibe o resultado
    elif operacao == '4':  # Se a operação for divisão
        if num2 != 0:  # Verifica se o divisor não é zero para evitar erro de divisão
            resultado = num1 / num2  # Realiza a divisão
            print(f"O resultado de {num1} / {num2} é: {resultado}")  # Exibe o resultado
        else:
            print("Erro: Divisão por zero não é permitida!")  # Mensagem de erro para divisão por zero
    else:  # Caso o usuário tenha inserido uma operação inválida
        print("Operação inválida! Por favor, escolha uma operação entre 1 e 4.")  # Mensagem de erro

# Chama a função da calculadora para iniciar o programa
calculadora()
