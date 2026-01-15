class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

    def ligar(self):
        print(f"Motor {self.potencia} ligado")


class Carro:
    def __init__(self, modelo, potencia_motor):
        self.modelo = modelo
        self.motor = Motor(potencia_motor)  # composição

    def ligar_carro(self):
        print(f"Carro {self.modelo} ligado")
        self.motor.ligar()

carro = Carro("Sedan", "2.0")
carro.ligar_carro()

class Professor:
    def __init__(self, nome):
        self.nome = nome


class Universidade:
    def __init__(self, nome):
        self.nome = nome
        self.professores = []

    def adicionar_professor(self, professor):
        self.professores.append(professor)

    def listar_professores(self):
        print(f"Professores da {self.nome}:")
        for prof in self.professores:
            print(prof.nome)

prof1 = Professor("Carlos")
prof2 = Professor("Ana")

universidade = Universidade("UFTech")
universidade.adicionar_professor(prof1)
universidade.adicionar_professor(prof2)

universidade.listar_professores()

class Autor:
    def __init__(self, nome):
        self.nome = nome

    def escrever_livro(self, titulo):
        return Livro(titulo, self)


class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def detalhes(self):
        print(f"Livro: {self.titulo} | Autor: {self.autor.nome}")
        
autor = Autor("Machado de Assis")
livro1 = autor.escrever_livro("Dom Casmurro")
livro2 = autor.escrever_livro("Memórias Póstumas")

livro1.detalhes()
livro2.detalhes()
