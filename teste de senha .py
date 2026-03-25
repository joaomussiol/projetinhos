print("=== cadastro ===")
username = input("Digite seu nome de usuário: ")
while True:
    username = input("Digite seu nome de usuário: ")

    if username.strip() == "":
        print("O nome de usuário não pode estar vazio")
    else:
        break
    
def senha_correta(user_password):
        number = any(char.isdigit() for char in user_password)
        upper = any(char.isupper() for char in user_password)
        especial_char = any(not char.isalnum() for char in user_password)

        if len(user_password) <8:
             print("A senha precisa de no minimo 8 caracteres")
             return False
        if not number:
             print("Precisa pelo menos ter um número")
        if not upper:
             print("Precisa pelo menos ter uma letra Maiúscula")
        if not especial_char:
             print("Precisa pelo menos ter um caractere especial")

        if number and upper and especial_char:
             return True
        else:
             return False
while True:
    user_password = (input("digite sua senha de usuario:"))
    if senha_correta(user_password):
        print("conta criada com sucesso")
        break

max_trys = 3

print("\n=== Login ===")

for tentativas in range(1, max_trys +1 ):
    username_digitado = input("Digite seu usuário: ")
    senha_digitada = (input("Digite sua senha:"))

    if username_digitado == username and senha_digitada == user_password:
        print("Login realizado com sucesso")
        break

    else:
        print(f"Erro! Tentativa {tentativas} de {max_trys}")

else:
    print("Limite de tentativas excedidas, Acesso Negado")