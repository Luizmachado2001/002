from bebidaquente import BebidaQuente
from bebidas.cafe import Cafe
from bebidas.cha import Cha
from bebidas.leite import Leite

from rich import inspect, print

def main():
    bebida = Cafe()
    inspect(bebida, methods=True)
    bebida.preparar()


if __name__ == "__main__":
    main()