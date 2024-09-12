# senha correta
senha_correta = "Pedro o melhor professor que ja tive"

# Inicia um loop infinito para continuar pedindo a senha até que a senha seja a certa
while True:
    # Solicita ao usuário que insira uma senha
    senha = input("Digite a senha: ")
    
    # Verifica se a senha inserida é a certa
    if senha == senha_correta:
        # Se a senha estiver correta, exibe uma mensagem de acesso permitido e encerra o loop
        print("Acesso permitido")
        break
    else:
        # Se a senha estiver errada, exibe uma mensagem de senha incorreta
        print("Senha incorreta")
