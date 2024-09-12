# Solicita ao usuário que insira um número
entrada = input("Digite um número inteiro positivo: ")

try:
    # Tenta converter a entrada para um número inteiro
    numero = int(entrada)
    
    # Verifica se o número é positivo
    if numero < 0:
        # Se o número for negativo, exibe uma mensagem de erro
        print("O número deve ser positivo.")
    else:
        # Inicializa a variável fatorial como 1 (o valor inicial para o cálculo do fatorial)
        fatorial = 1
        
        # Loop para calcular o fatorial
        for i in range(1, numero + 1):
            # Multiplica o valor atual do fatorial pelo número corrente no loop
            fatorial *= i
        
        # Exibe o resultado do cálculo do fatorial
        print(f"O fatorial de {numero} é {fatorial}.")
        
except ValueError:
    # Se a conversão falhar, exibe uma mensagem de erro
    print("Entrada inválida. Por favor, insira um número inteiro positivo.")