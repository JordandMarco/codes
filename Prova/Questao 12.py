def conta_vogais(texto):
 
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador

texto = input("Digite um texto: ")

quantidade = conta_vogais(texto)

print(f"Quantidade de vogais: {quantidade}")

print("Quantidade de vogais: {}".format(quantidade))
