import Fila
class FilaP():
    def __init__(self):
        self.f1 = Fila.Fila()
        self.f2 = Fila.Fila()
        self.cont = 0
    def inserir(self,valor,prio):
        if prio == 1:
            self.f1.inserir(valor)  
        elif prio == 2:
            self.f2.inserir(valor)
        self.cont +=1
    def show(self):
        self.f1.show()
        self.f2.show()
    def remover(self):
        if not self.f1.estahvazia():
            self.f1.remove()
        else:
            self.f2.remove()
    def getPrim(self):
        if self.f1.quant > 0:
            return self.f1.getPrim()  
        elif self.f2.quant > 0:
            return self.f2.getPrim()
