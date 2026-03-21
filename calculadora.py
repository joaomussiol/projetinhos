def calcular(num1, operador, num2):
        if operador == "+" :
            return num1 + num2
    
        elif operador == "-" :
            return num1 - num2
    
        elif operador == "*" :
            return num1 * num2
    
        elif operador == "/":
            if num2 == 0:
                print("ERRO, DIVISÃO POR ZERO")
                return None
            else:
                return num1 / num2
        else:
            print("Operador inválido")
            return None

while True:
    try:
        num1 = float(input("Digite o primeiro numero: "))
        operador = input("Digite um operador. Ele pode ser. +, -, *, / : ")
        num2 = float(input("Digite o segundo numero: "))

    except ValueError:
        print("Insira apenas valores corretos")
        continue
    resultado = calcular(num1, operador, num2)

    if resultado is not None:
        print(f"{num1} {operador} {num2} = {resultado:.3f}")

    continuar = input("Deseja continuar? (S/N): ").lower().strip()

    while continuar not in ["s", "n" ]:
        continuar = input("Digite apenas S ou N: ").lower().strip()

    if continuar == ("n"):
        break