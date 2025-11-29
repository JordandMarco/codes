# Soma de dois numeros utilizando funcao

def soma(a, b):
    return a + b

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
print("Resultado da soma:", soma(num1, num2))

# Funcao para mostrar se o numero é par 

def eh_par(numero):
    return numero % 2 == 0

num = int(input("Digite um número: "))
print("É par?", eh_par(num))

# Funcao para calcular a media de uma lista

def media(lista):
    return sum(lista) / len(lista)

numeros = [10, 8, 7, 9, 6]
print("Média:", media(numeros))


def saudacao(nome):
    print(f"Olá, {nome}! Seja bem-vindo(a)!")

saudacao("Jordan")
