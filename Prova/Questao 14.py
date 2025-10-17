def coletar_nomes():

    nomes = []
    while True:
        nome = input("Digite um nome (ou 'sair' para encerrar): ")
        if nome.lower() == "sair":
            break
        nomes.append(nome)
    return nomes

lista_nomes = coletar_nomes()

print(f"\nLista de nomes coletados: {lista_nomes}")

print("Lista de nomes coletados: {}".format(lista_nomes))
