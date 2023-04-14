"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores de sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista
"""
lista_compras = []
print("=-"*6,"LISTA DE COMPRAS","=-"*6 )
while True:
    print("- Selecione uma opção:")
    opcao = input("[i]nserir  [a]pagar  [l]istar  [s]air: ")
    if opcao == "s":
        print("LISTA ENCERRADA!")
        break
    while opcao != "i" and opcao != "a" and opcao != "l" and opcao != "s":
        print("Escolha APENAS estas opções:")
        opcao = input("[i]nserir  [a]pagar  [l]istar  [s]air: ")
        
    if opcao == "i":
        item_novo = input("Digite o item que deseja adicionar a lista: ")
        lista_compras.append(item_novo)
        print("\n")
    
    elif opcao == "a":
        del_item = input("Digite o índice do item para deletar da lista: ")
        try:
            del_item_int = int(del_item)
            del lista_compras[del_item_int]
            print("\n")
        except:
            print("ÍNDICE INEXISTENTE!", end= "\n")
            continue

    elif opcao == "l":
        print("Sua lista:")
        for indice, item in enumerate(lista_compras):
            print(indice, item)
            print("\n")
            

    elif opcao == "s":
            print("LISTA ENCERRADA!")
            break 
