alunos = {"Ana": 8, "João": 6, "Pedro": 9}

while True:
    entrada = input("Digite 'sair' para encerrar ou pressione Enter para verificar os alunos: ")
    if entrada.lower() == "sair":
        break

    for nome, nota in alunos.items():
        situacao = "Aprovado" if nota >= 7 else "Reprovado"
        print(f"O aluno {nome} obteve nota {nota} e está {situacao}.")
        print("Aluno: {} | Nota: {} | Situação: {}".format(nome, nota, situacao))
