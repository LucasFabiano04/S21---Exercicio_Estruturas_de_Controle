# Função principal para imprimir números pares e ímpares
def numeros_pares_impares():
    try:
        # Solicita um número ao usuário e converte a entrada para um número inteiro
        limite = int(input("Digite um número: "))
    except ValueError:
        # Captura erro se a entrada não for um número inteiro
        print("Entrada inválida! Por favor, insira um número inteiro.")
        return  # Termina a função se a entrada for inválida

    # Laço de repetição para percorrer todos os números de 1 até o número inserido pelo usuário
    for numero in range(1, limite + 1):
        # Estrutura de seleção para verificar se o número é par ou ímpar
        if numero % 2 == 0:  # Se o número é divisível por 2 (ou seja, é par)
            print(f"{numero} é par")  # Imprime que o número é par
        else:  # Se o número não é divisível por 2 (ou seja, é ímpar)
            print(f"{numero} é ímpar")  # Imprime que o número é ímpar

# Chama a função para iniciar o programa
numeros_pares_impares()
