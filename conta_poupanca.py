from conta import *

class ContaPoupanca(Conta):

    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
            self._extrato.append(f"Saque: R${valor:.2f}")
        else:
            print("Saldo insuficiente!")

    def tipo(self):
        return "Conta Poupança"
    
    def render_juros(self):
        self._saldo = self._saldo + (self._saldo * 0.6 / 100)