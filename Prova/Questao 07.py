
texto = input("Digite uma string: ")

contador_maiusculas = 0

for caractere in texto:
    if caractere.isupper():  # Verifica se o caractere é letra maiúscula
        contador_maiusculas += 1

print(f"Número de letras maiúsculas: {contador_maiusculas}")
print("Número de letras maiúsculas: {}".format(contador_maiusculas))
