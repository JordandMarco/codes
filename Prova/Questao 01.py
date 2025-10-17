while True:
    numeros = []

    for i in range(5):
        entrada = input(f"Digite o {i+1}º número (ou 'sair' para encerrar): ")
        if entrada.lower() == "sair":
            print("Programa encerrado.")
            exit()
        numeros.append(int(entrada))

    soma = 0
    maior = numeros[0]
    menor = numeros[0]

    for n in numeros:
        soma += n
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

    print(f"\nResultados (usando f-string):")
    print(f"Soma = {soma}")
    print(f"Maior = {maior}")
    print(f"Menor = {menor}")

 
    print("\nResultados (usando format()):")
    print("Soma = {}".format(soma))
    print("Maior = {}".format(maior))
    print("Menor = {}\n".format(menor))
