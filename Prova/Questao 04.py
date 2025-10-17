while True:
    palavra = input("Digite uma palavra (ou 'sair' para encerrar): ")
    if palavra.lower() == "sair":
        break

    vogais = "aeiou"
    contador = 0

    for letra in palavra.lower():
        if letra in vogais:
            contador += 1

    print(f"A palavra '{palavra}' possui {contador} vogais.")
    print("A palavra '{}' possui {} vogais.".format(palavra, contador))
