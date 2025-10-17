def resultado_alunos(alunos):
 
    resultados = {}
    for nome, nota in alunos.items():
        if nota >= 7:
            resultados[nome] = "Aprovado"
        else:
            resultados[nome] = "Reprovado"
    return resultados

alunos = {}
print("Digite as notas dos alunos (3 alunos):")
for i in range(3):
    nome = input(f"Nome do {i+1}º aluno: ")
    nota = float(input(f"Nota de {nome}: "))
    alunos[nome] = nota

resultados = resultado_alunos(alunos)


print("\nUsando f-string:")
for nome, status in resultados.items():
    print(f"{nome}: {status}")

print("\nUsando format():")
for nome, status in resultados.items():
    print("{}: {}".format(nome, status))
