# Calculadora com while
while True:
    try:

        numero_1 = input("Digite o primeiro número: ")
        while numero_1 == "":
            print("primeiro número vazio!")
            numero_1 = input("Digite o primeiro número: ")
        if numero_1 == "sair":
            print("Você saiu do sistema!")
            break
        numero_um=float(numero_1)

        print("operadores possiveis +, -, *, /, %")
        operacao = input("Digite a operação a ser executada: ")
        if operacao == "sair":
            print("Você saiu do sistema!")
            break
        while operacao != "+" and operacao != "-" and operacao != "*" and operacao != "/" and operacao != "%":
            print("Digite uma operação valida!(+, -, *, /, %)")
            operacao = input("Digite a operação a ser executada: ")

        numero_2 = input ("Digite o segundo número: ")
        while numero_2 == "":
            print("segundo número vazio!")
            numero_2 = input ("Digite o segundo número: ")
        if numero_2 == "sair":
            print("Você saiu do sistema!")
            break
        numero_dois=float(numero_2)

        resultado = ""

        if operacao == "+":
            resultado = numero_um + numero_dois
            print (f"{numero_um} {operacao} {numero_dois} = {resultado}")
        elif operacao == "-":
            resultado = numero_um - numero_dois
            print (f"{numero_um} {operacao} {numero_dois} = {resultado}")
        elif operacao == "*":
            resultado = numero_um * numero_dois
            print (f"{numero_um} {operacao} {numero_dois} = {resultado}")
        elif operacao == "/":
            if numero_dois == 0:
                print("NÃO É POSSIVEL DIVIDIR POR ZERO")
                continue
            resultado = numero_um / numero_dois
            print (f"{numero_um} {operacao} {numero_dois} = {resultado}")
        elif operacao == "%":
            resultado = numero_um % numero_dois
            print (f"o resto da divisão de {numero_um} por {numero_dois} é {resultado}")
        else:
            print("OPERAÇÃO INVALIDA!")

    except:
        print("DIGITE UM NÚMERO VALIDO!")
        continue