# Numero Positivo 

num = int(input("Digite um número: "))
if num > 0:
    print("O número é positivo.")
elif num == 0:
    print("O número é zero.")
else:
    print("O número é negativo.")

# Maioridade

idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# Nota escolar

nota = float(input("Digite sua nota (0 a 10): "))
if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")

# Número positivo, par e múltiplo de 5

num = int(input("Digite um número: "))
if num > 0:
    print("O número é positivo.")
    if num % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")
    if num % 5 == 0:
        print("O número é múltiplo de 5.")
else:
    print("O número não é positivo.")

# Semáforo

cor = input("Digite a cor do semáforo (verde, amarelo, vermelho): ").lower()
if cor == "verde":
    print("Pode seguir.")
elif cor == "amarelo":
    print("Atenção, reduza a velocidade.")
elif cor == "vermelho":
    print("Pare!")
else:
    print("Cor inválida.")

# Idade e habilitação

idade = int(input("Digite sua idade: "))
if idade >= 18:
    habilitacao = input("Você tem habilitação? (sim/não): ").lower()
    if habilitacao == "sim":
        print("Você pode dirigir.")
    else:
        print("Você não pode dirigir.")
else:
    print("Você é menor de idade e não pode dirigir.")

# Par ou Ímpar em uma linha

num = int(input("Digite um número: "))
print("Par" if num % 2 == 0 else "Ímpar")

# Número entre 10 e 20

num = int(input("Digite um número: "))
if 10 <= num <= 20:
    print("O número está entre 10 e 20.")
else:
    print("O número não está entre 10 e 20.")

# Maior de três números

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
if a >= b and a >= c:
    print("O maior número é:", a)
elif b >= a and b >= c:
    print("O maior número é:", b)
else:
    print("O maior número é:", c)

# Usuário e senha

usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")
if usuario == "admin" and senha == "1234":
    print("Acesso permitido")
else:
    print("Acesso negado")
