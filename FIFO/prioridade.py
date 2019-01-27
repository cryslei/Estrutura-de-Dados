class No():
    def __init__(self,valor,proximo):
        self.info = valor
        self.prox = proximo
class FIFO_dinamica_sequencial():
    def __init__(self):
        self.prim = None
        self.ult = None
        self.velha = []
        self.gestante = []
        self.prioridadeG = 0
        self.deficiente = []
        self.prioridadeD = 0
        self.normal = []
        self.prioridadeN = 0
        
        self.quant = 0
    def inserir(self,valor):
        if self.quant == 0:
            self.prim=self.ult=No(valor,None)
        else:
            self.ult.prox=self.ult=No(valor,None)
        self.quant+=1
    def remove(self):
        if self.quant == 1:
            self.prim=self.ult= None
        else:
            self.prim = self.prim.prox
        self.quant-=1
    def getPrim(self):
        for x in self.quant:
            if self.prioridadeG > 0:
                pass
        return self.prim.info
    def estahvazia(self):
        return self.quant == 0
