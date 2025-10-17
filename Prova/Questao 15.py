
def conta_maiusculas(texto):

    contador = 0
    for letra in texto:
        if letra.isupper():
            contador += 1
    return contador

texto = input("Digite um texto: ")

quantidade_maiusculas = conta_maiusculas(texto)

print(f"Quantidade de letras maiúsculas: {quantidade_maiusculas}")

print("Quantidade de letras maiúsculas: {}".format(quantidade_maiusculas))
