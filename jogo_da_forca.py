"""
-=-=-=-=-JOGO DA FORCA-=-=-=-=
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
-Faça a contagem de tentativas do seu
usuário.
-Coloque apenas 20 tentativas máximas
"""

palavra_secreta = "python"
letras_acertadas = ""
numero_tentativas = 0 

print("\n***JOGO DA FORCA***\n")

while True:
    numero_tentativas += 1
    if numero_tentativas > 20:
        print("número máximo de tentativas alcançado")
        break
        
    letra_digitada = input("Digite uma letra: ").lower()
    

    if numero_tentativas > 20:
        break
    if len(letra_digitada)>1:
        print("Digite apenas uma letra.")
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ""
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"
    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        print("VOCÊ GANHOU!!")
        print(f"número de tentativas: {numero_tentativas}")
        break
