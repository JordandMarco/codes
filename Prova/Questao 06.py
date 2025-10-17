nomes = []

while True:
    nome = input("Digite um nome (ou 'sair' para encerrar): ")
    if nome.lower() == "sair":
        break
    nomes.append(nome)

print(f"\nOs nomes digitados foram: {nomes}")
print("Lista final de nomes: {}".format(nomes))
