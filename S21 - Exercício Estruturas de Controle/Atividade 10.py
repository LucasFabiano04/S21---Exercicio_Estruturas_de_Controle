# Pede um número ao usuário
numero = int(input("Digite um número positivo: "))

# Verifica se o número é maior que 0
if numero > 0:
    print(f"Tabuada do {numero}:")  # Mostra qual tabuada vai ser exibida
    
    # Faz um loop de 1 a 10 para imprimir a tabuada
    for i in range(1, 11):
        resultado = numero * i  # Calcula o resultado da multiplicação
        print(f"{numero} x {i} = {resultado}")  # Mostra o resultado
else:
    # Se o número não for maior que 0, mostra uma mensagem de erro
    print("Número inválido. Digite um número maior que 0.")
