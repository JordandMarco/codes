#1.QUESTAO
class Animal:
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        print("Au au!")

class Gato(Animal):
    def falar(self):
        print("Miau!")

# Lista de animais
animais = [Cachorro(), Gato(), Cachorro(), Gato()]

# Chamando o método falar()
for animal in animais:
    animal.falar()

#2.QUESTAO
import math

class Forma:
    def area(self):
        pass

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * self.raio ** 2

def mostrar_areas(formas):
    for forma in formas:
        print(f"Área: {forma.area():.2f}")

formas = [Quadrado(4), Circulo(3), Quadrado(2)]
mostrar_areas(formas)

#3.QUESTAO 
class Funcionario:
    def salario(self):
        pass

class Gerente(Funcionario):
    def salario(self):
        return 5000

class Estagiario(Funcionario):
    def salario(self):
        return 1500

funcionarios = [Gerente(), Estagiario(), Estagiario(), Gerente()]

for funcionario in funcionarios:
    print(f"Salário: R$ {funcionario.salario():.2f}")

#4.QUESTAO 
class Veiculo:
    def mover(self):
        pass

class Carro(Veiculo):
    def mover(self):
        print("Dirigindo...")

class Bicicleta(Veiculo):
    def mover(self):
        print("Pedalando...")

class Aviao(Veiculo):
    def mover(self):
        print("Voando...")

# Lista de veículos
veiculos = [Carro(), Bicicleta(), Aviao(), Carro()]

# Chamando mover()
for veiculo in veiculos:
    veiculo.mover()
