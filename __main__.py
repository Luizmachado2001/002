from bebidaquente import BebidaQuente
from bebidas.cafe import Cafe
from bebidas.cha import Cha
from bebidas.leite import Leite

from rich import print,console

def main():

    bebida_cafe = Cafe()
    bebida_cafe.preparar()

    bebida_leite = Leite()
    bebida_leite.preparar()

    bebida_cha = Cha()
    bebida_cha.preparar()


if __name__ == "__main__":
    main()