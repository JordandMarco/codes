from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor):
        self.valor = valor

    @abstractmethod
    def processar_pagamento(self):
        pass

class Cancelavel(ABC):

    @abstractmethod
    def cancelar_pagamento(self):
        pass

class CartaoCredito(Pagamento, Cancelavel):
    def processar_pagamento(self):
        print(f"Pagamento de R$ {self.valor:.2f} processado no cartão de crédito.")

    def cancelar_pagamento(self):
        print("Pagamento no cartão de crédito cancelado.")

class Pix(Pagamento, Cancelavel):
    def processar_pagamento(self):
        print(f"Pagamento de R$ {self.valor:.2f} processado via Pix.")

    def cancelar_pagamento(self):
        print("Pagamento via Pix cancelado.")

class Boleto(Pagamento, Cancelavel):
    def processar_pagamento(self):
        print(f"Boleto no valor de R$ {self.valor:.2f} gerado.")

    def cancelar_pagamento(self):
        print("Boleto cancelado.")

pagamentos = [
    CartaoCredito(150.00),
    Pix(80.50),
    Boleto(200.00)
]

for pagamento in pagamentos:
    pagamento.processar_pagamento()
    pagamento.cancelar_pagamento()
    print("-" * 30)
