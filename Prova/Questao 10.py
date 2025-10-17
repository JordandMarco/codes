def media_turma(notas):
  
    media = sum(notas) / len(notas)
    
    if media >= 9:
        classificacao = "Excelente"
    elif media >= 7:
        classificacao = "Bom"
    elif media >= 5:
        classificacao = "Regular"
    else:
        classificacao = "Ruim"
    
    return media, classificacao

notas = []

print("Digite as notas dos alunos:")

for i in range(3):
    n = float(input(f"Digite a nota do {i+1}º aluno: "))
    notas.append(n)

# Converte para tupla
notas_tupla = tuple(notas)

# Chama a função
media, classificacao = media_turma(notas_tupla)

# Mostrando resultados usando f-string
print(f"\nUsando f-string -> Média da turma: {media:.2f}, Classificação: {classificacao}")

# Mostrando resultados usando format()
print("Usando format() -> Média da turma: {:.2f}, Classificação: {}".format(media, classificacao))
