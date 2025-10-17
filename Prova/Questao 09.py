def analise_lista(numeros):

    soma = sum(numeros)
    maior = max(numeros)
    menor = min(numeros)
    return soma, maior, menor

numeros = []

print("Digite 5 números inteiros:")
for i in range(5):
    n = int(input(f"Digite o {i+1}º número: "))
    numeros.append(n)

soma, maior, menor = analise_lista(numeros)

print(f"\nUsando f-string -> Soma: {soma}, Maior: {maior}, Menor: {menor}")

print("Usando format() -> Soma: {}, Maior: {}, Menor: {}".format(soma, maior, menor))
