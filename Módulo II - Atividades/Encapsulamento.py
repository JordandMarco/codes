#1.QUESTAO 
class ContaBancaria:
    def __init__(self):
        self.__saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor

    def ver_saldo(self):
        return self.__saldo

conta = ContaBancaria()
conta.depositar(100)
conta.sacar(30)
print(conta.ver_saldo())

#2.QUESTAO
class Pessoa:
    def __init__(self, nome, anoNasceu):
        self.nome = nome
        self._anoNasceu = anoNasceu   

pessoa = Pessoa("Ana", 2005)

print(pessoa.nome)         
print(pessoa._anoNasceu)    

#3.QUESTAO
class ContaBancaria:
    def __init__(self):
        self.__saldo = 0

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor

conta = ContaBancaria()
conta.saldo = 200
print(conta.saldo)

conta.saldo = -50  
print(conta.saldo)

#4.QUESTAO
class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco if preco >= 0 else 0

    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):
        if valor >= 0:
            self.__preco = valor

produto = Produto("Caderno", 15.0)

print(produto.nome)     
print(produto.preco)    

produto.preco = 20.0    
print(produto.preco)

produto.preco = -5    
print(produto.preco)

