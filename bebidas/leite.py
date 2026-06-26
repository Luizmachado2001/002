from bebidaquente import BebidaQuente

class Leite(BebidaQuente):
    def __init__(self):
        pass

    def servir(self):
        print("2. Passando vapor pressurizado pelo bico do leite.")
        self.preparar()
        
    def misturar(self):
        print("3. Servindo na caneca grande, já com café.")