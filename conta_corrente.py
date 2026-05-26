from conta import *

class ContaCorrente(Conta):

    def sacar(self, valor):
        taxa = valor * 5 / 100
        if valor + taxa <= self._saldo:
            self._saldo -= valor + taxa
            self._extrato.append(f"Saque: R${valor:.2f} | Taxa: R${taxa:.2f}")
        else:
            print("Saldo insuficiente!")

    def tipo(self):
        return "Conta Corrente"
       