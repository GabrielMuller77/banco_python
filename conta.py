from abc import ABC, abstractmethod

class Conta(ABC):

    def __init__(self, titular, _saldo = 0):
        self.titular = titular
        self._saldo = _saldo
        self._extrato = []

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def tipo(self):
        pass

    def depositar(self, valor):
        self._saldo += valor
        self._extrato.append(f"Depósito: R${valor:.2f}")

    def ver_extrato(self):
        print(f"---EXTRATO: {self.tipo()}: {self.titular}")
        for item in self._extrato:
            print(item)
        print(f"Saldo atual: R${self._saldo:.2f}")