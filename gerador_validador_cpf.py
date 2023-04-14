import os
from random import randint

while True:
    print("Escolha uma opção:")
    opcao = input("[1]gerar um cpf [2]verificar a validade de um cpf: ")
    if opcao == "1":
        soma_nove_dig = 0
        soma_dez_dig = 0

        n = 0
        numeros = []
        while n < 10:
            numeros.append(n)
            n += 1

        i = 0
        cpf = []
        while i < 9:
            num_sortido = randint(0 , 9)
            cpf.append(num_sortido)
            i += 1

        multiplo_regressivo = 10
        for digito in cpf:
            soma_nove_dig += digito * multiplo_regressivo
            multiplo_regressivo -= 1

        vezes_dez = soma_nove_dig * 10
        resto_por_onze = vezes_dez % 11

        decimo_digito = resto_por_onze if resto_por_onze <= 9 else 0
        cpf.append(decimo_digito)

        multiplo_regressivo = 11
        for digito in cpf:
            soma_dez_dig += digito * multiplo_regressivo
            multiplo_regressivo -= 1

        vezes_dez = soma_dez_dig * 10
        resto_por_onze = vezes_dez % 11
        ultimo_digito = resto_por_onze if resto_por_onze <= 9 else 0
        cpf.append(ultimo_digito)

        os.system("clear")
        print("CPF gerado aleatoriamente:", *cpf)

    elif opcao == "2":
        os.system("clear")
        soma_nove_dig = 0
        soma_dez_dig = 0
        arroz = True
        while arroz:
            try:
                cpf = input("Digite o cpf: ")
                testando_int = int(cpf)
                nove_digitos_cpf = cpf[:9]
                arroz = False
            except ValueError:
                print("Digite somente números!")

        multiplo_regressivo = 10
        for digito in nove_digitos_cpf:
            soma_nove_dig += int(digito) * multiplo_regressivo
            multiplo_regressivo -= 1
            
        vezes_dez = soma_nove_dig * 10
        resto_por_onze = vezes_dez % 11

        decimo_digito = resto_por_onze if resto_por_onze <= 9 else 0


        dez_digitos_cpf = nove_digitos_cpf + str(decimo_digito)
        multiplo_regressivo = 11
        for digito in dez_digitos_cpf:
                soma_dez_dig += int(digito) * multiplo_regressivo
                multiplo_regressivo -= 1

        vezes_dez = soma_dez_dig * 10
        resto_por_onze = vezes_dez % 11
        ultimo_digito = resto_por_onze if resto_por_onze <= 9 else 0
        
        if cpf == nove_digitos_cpf + str(decimo_digito) + str(ultimo_digito):
            print("CPF VALIDO!")
        else:
            print("CPF INVALIDO!")
    