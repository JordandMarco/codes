notas = (7.5, 8.0, 5.0, 9.0, 6.5)

while True:
    entrada = input("Digite 'sair' para encerrar ou pressione Enter para calcular a média: ")
    if entrada.lower() == "sair":
        break

    media = sum(notas) / len(notas)

    if media >= 9:
        desempenho = "Excelente"
    elif media >= 7:
        desempenho = "Bom"
    elif media >= 5:
        desempenho = "Regular"
    else:
        desempenho = "Ruim"

    print(f"A média da turma é {media:.2f} - {desempenho}")
    print("Classificação da turma: {}".format(desempenho))
