# 1. QUESTAO
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

# 2. QUESTAO
class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def latir(self):
        print(f"Au au, meu nome é {self.nome} e tenho {self.idade} anos")

cachorro1 = Cachorro("Rex", 3)
cachorro1.latir()

#3. QUESTAO
class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def mostrar_informacoes(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano: {self.ano}")
        print("-" * 30)

livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
livro2 = Livro("1984", "George Orwell", 1949)
livro3 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943)

livro1.mostrar_informacoes()
livro2.mostrar_informacoes()
livro3.mostrar_informacoes()

#4. QUESTAO 
class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano

    def dirigir(self):
        print("O carro está em movimento")

carro1 = Carro("Fusca", 1975)
carro1.dirigir()

#5. QUESTAO
class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def latir(self):
        print(f"Au au, meu nome é {self.nome} e tenho {self.idade} anos")

    def aniversario(self):
        self.idade += 1
        print(f"{self.nome} fez aniversário! Agora tem {self.idade} anos")

cachorro1 = Cachorro("Rex", 3)
cachorro1.latir()
cachorro1.aniversario()

#6. QUESTAO
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor <= 0:
            print("O valor do saque deve ser positivo.")
        elif valor > self.saldo:
            print("Saldo insuficiente. Operação não realizada.")
        else:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    def mostrar_saldo(self):
        print(f"Titular: {self.titular} | Saldo: R$ {self.saldo:.2f}")

conta = ContaBancaria("João", 100)
conta.mostrar_saldo()
conta.depositar(50)
conta.sacar(30)
conta.sacar(200)
conta.mostrar_saldo()

#7. QUESTAO
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Estudante(Pessoa):
    def __init__(self, nome, idade, matricula, curso):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.curso = curso

#8. QUESTAO
class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def calcular_decimo_terceiro(self):
        return self.salario

#9. QUESTAO
class Professor(Funcionario):
    def __init__(self, nome, idade, salario, disciplina):
        super().__init__(nome, idade, salario)
        self.disciplina = disciplina

    def lecionar(self):
        print(f"Professor {self.nome} leciona {self.disciplina}")

#10. QUESTAO
class Artista:
    def apresentar(self):
        print("Sou artista")

class Programador:
    def apresentar(self):
        print("Sou programador")

class PessoaMultiTalento(Artista, Programador):
    pass

pessoa = PessoaMultiTalento()
pessoa.apresentar()

#11. Questao
class Artista:
    def apresentar(self):
        print("Sou artista")
        super().apresentar()

class Programador:
    def apresentar(self):
        print("Sou programador")

class PessoaMultiTalento(Artista, Programador):
    def apresentar(self):
        print("Sou multitarefa")
        super().apresentar()

pessoa = PessoaMultiTalento()
pessoa.apresentar()

#12. Questao
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        if self.notas:
            return sum(self.notas) / len(self.notas)
        return 0
    
class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina, salario):
        super().__init__(nome, idade)
        self.disciplina = disciplina
        self.salario = salario

# Criando aluno
aluno1 = Aluno("Maria", 16, "A123")
aluno1.adicionar_nota(8.5)
aluno1.adicionar_nota(7.0)
aluno1.adicionar_nota(9.0)

# Criando professor
professor1 = Professor("Carlos", 40, "Matemática", 3500)

# Exibindo dados
print("=== ALUNO ===")
print(f"Nome: {aluno1.nome}")
print(f"Idade: {aluno1.idade}")
print(f"Matrícula: {aluno1.matricula}")
print(f"Média: {aluno1.calcular_media():.2f}")

print("\n=== PROFESSOR ===")
print(f"Nome: {professor1.nome}")
print(f"Idade: {professor1.idade}")
print(f"Disciplina: {professor1.disciplina}")
print(f"Salário: R$ {professor1.salario:.2f}")
