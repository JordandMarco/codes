def operacoes(a, b):

    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    divisao = a / b if b != 0 else "Divisão por zero não é permitida"
    return soma, subtracao, multiplicacao, divisao

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

soma, subtracao, multiplicacao, divisao = operacoes(a, b)

print(f"\nUsando f-string -> Soma: {soma}, Subtração: {subtracao}, Multiplicação: {multiplicacao}, Divisão: {divisao}")

print("Usando format() -> Soma: {}, Subtração: {}, Multiplicação: {}, Divisão: {}".format(soma, subtracao, multiplicacao, divisao))
