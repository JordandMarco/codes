# Mostrar todos os numeros pares de 1 a 20

for num in range(1, 21):
    if num % 2 == 0:
        print(num)

# Ler 5 numeros e mostrar o maior entre eles 

maior = None

for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    if maior is None or num > maior:
        maior = num

print("O maior número digitado foi:", maior)

# Mostrar vogais 

texto = input("Digite uma frase ou palavra: ")
vogais = "aeiouAEIOU"
contador = 0

for letra in texto:
    if letra in vogais:
        contador += 1

print("A quantidade de vogais é:", contador)

