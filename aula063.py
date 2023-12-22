class Conta(object):
    def __init__(self, ID, saldo):
        self.ID = ID
        self.saldo = saldo
    def __str__(self):
        return f'ID: {self.ID} \nSaldo: R${self.saldo}'
    def __add__(self, other):
        self.saldo += other.saldo

conta_1 = Conta(100, 2500)
conta_2 = Conta(101, 1000)
conta_1.__add__(conta_2)
print(conta_1.saldo)

