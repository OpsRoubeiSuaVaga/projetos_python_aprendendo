import os
from random import randint

while True:
    print("Escolha uma opção:")
    opcao = input("[1]Gerar um cpf [2]Verificar a validade de um cpf: ")
    if opcao == "1":
        soma_nove_dig = 0
        soma_dez_dig = 0

        n = 0
        numeros = ""
        while n < 10:
            numeros += str(n)
            n += 1

        i = 0
        cpf = ""
        while i < 9:
            num_sortido = randint(0 , 9)
            cpf += str(num_sortido)
            i += 1

        multiplo_regressivo = 10
        for digito in cpf:
            soma_nove_dig += int(digito) * multiplo_regressivo
            multiplo_regressivo -= 1

        vezes_dez = soma_nove_dig * 10
        resto_por_onze = vezes_dez % 11
        decimo_digito = resto_por_onze if resto_por_onze <= 9 else 0
        

        multiplo_regressivo = 11
        for digito in cpf:
            soma_dez_dig += int(digito) * multiplo_regressivo
            multiplo_regressivo -= 1

        vezes_dez = soma_dez_dig * 10
        resto_por_onze = vezes_dez % 11
        ultimo_digito = resto_por_onze if resto_por_onze <= 9 else 0

        os.system("clear")
        print(f"CPF gerado aleatoriamente: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{decimo_digito}{ultimo_digito}")

    elif opcao == "2":
        os.system("clear")
        soma_nove_dig = 0
        soma_dez_dig = 0
        arroz = True
        while arroz:
            try:
                cpf = input("Digite o cpf(somente números): ") 
                testando_int = int(cpf)
                cpf_repetido_true = cpf == str(cpf[0] * (len(cpf)))
                if cpf_repetido_true:
                    print("NÃO REPITA TODOS OS NÚMEROS!")
                    continue
                arroz = False
            except ValueError:
                print("Digite somente números!")
        
        nove_digitos_cpf = cpf[:9]
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
    