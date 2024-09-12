import random  # Importa a biblioteca para gerar números aleatórios

# O computador escolhe um número aleatório entre 1 e 50
numero_secreto = random.randint(1, 50)

# O usuário tem até 5 tentativas para adivinhar o número
tentativas_restantes = 5

# Início do loop de tentativas
while tentativas_restantes > 0:
    # Pede ao usuário que insira um palpite
    palpite = int(input("Adivinhe um número entre 1 e 50: "))
    
    # Verifica se o palpite está correto
    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número!")
        break  # Encerra o loop se o palpite estiver correto
    elif palpite < numero_secreto:
        # Fala para o usuário que o número secreto é maior que o palpite
        print("O número é maior que o seu palpite.")
    else:
        # Fala para o usuário que o número secreto é menor que o palpite
        print("O número é menor que o seu palpite.")
    
    # Diminui o número de tentativas que sobraram
    tentativas_restantes -= 1

# Mensagem final se a pessoa não acertar o número
if tentativas_restantes == 0:
    print(f"Você perdeu! O número secreto era {numero_secreto}.")
