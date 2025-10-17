def calcular_operacoes(a, b):
    soma = a + b
    sub = a - b
    mult = a * b
    div = a / b if b != 0 else "Divisão por zero"
    return soma, sub, mult, div


while True:
    sair = input("Digite 'sair' para encerrar ou pressione Enter para continuar: ")
    if sair.lower() == "sair":
        break

    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    soma, sub, mult, div = calcular_operacoes(n1, n2)

    print(f"Soma: {soma}")
    print("Subtração: {}".format(sub))
    print(f"Multiplicação: {mult}")
    print("Divisão: {}".format(div))
