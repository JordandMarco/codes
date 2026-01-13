# 1. Classe Carro
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def dirigir(self):
        print("O carro está em movimento")

carro1 = Carro("Toyota", "Corolla")
carro2 = Carro("Honda", "Civic")
print(carro1.marca, carro1.modelo)
print(carro2.marca, carro2.modelo)
carro1.dirigir()

