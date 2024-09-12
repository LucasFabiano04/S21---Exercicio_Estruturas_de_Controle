# Pede o peso do usuário e o converte para um número
peso = float(input("Digite seu peso (em kg): "))

# Pede a altura do usuário e a converte para um número 
altura = float(input("Digite sua altura (em metros): "))

# Calcula o IMC usando a fórmula: peso / (altura ** 2)
imc = peso / (altura ** 2)

# Exibe o valor calculado do IMC
print(f"Seu IMC é: {imc:.2f}")

# Classifica o IMC com base em dados específicos
if imc < 18.5:  # Abaixo do peso
    print("Classificação: Abaixo do peso")
elif 18.5 <= imc < 24.9:  # Peso normal
    print("Classificação: Peso normal")
elif 25 <= imc < 29.9:  # Sobrepeso
    print("Classificação: Sobrepeso")
else:  # Obesidade
    print("Classificação: Obesidade")
