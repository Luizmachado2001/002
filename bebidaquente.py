from abc import ABC, abstractmethod

class BebidaQuente(ABC):
    def __init__(self) -> None:
        pass

    def preparar(self):
        print(3*"-", " Iniciando o Preparo ", 3 * "-")
        print("1. Fervendo água a 100 graus Celsius.")
        print(3*"-", " Bebida Pronta", 3 * "-")

    def ferver_agua(self):
        pass

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass