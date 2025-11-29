# Soma de todos os numeros ate digitar 0

soma = 0
num = int(input("Digite um número (0 para sair): "))

while num != 0:
    soma += num
    num = int(input("Digite um número (0 para sair): "))

print("A soma dos números digitados é:", soma)

# Digitar a senha correta

senha = ""
while senha != "python123":
    senha = input("Digite a senha: ")

print("Senha correta! Acesso permitido.")

# Tabuada utilizando WHILE

numero = int(input("Digite um número para ver a tabuada: "))
i = 1

while i <= 10:
    print(f"{numero} x {i} = {numero * i}")
    i += 1
