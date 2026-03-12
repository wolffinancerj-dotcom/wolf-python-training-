def verificar_senha(teste_senha, senha):
    return teste_senha == senha

senha = "0000"

tries = 0
while tries < 3:
    teste_senha = input("Digite sua senha: ")
    if verificar_senha(teste_senha, senha):
        print("Você entrou!")
        break
    else:
        tries += 1
        if tries < 3:
            print(f"Você tem {3 - tries} tentativas restantes.")
        else:
            print("Acesso bloqueado.")


