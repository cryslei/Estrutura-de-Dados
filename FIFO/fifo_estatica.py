class FIFO_Estatica():
    def __init__(self):
        self.lista = [None,None,None,None,None]
        self.quant = 0
    def remover(self):
        for x in range(self.quant-1):
            self.lista[x] = self.lista[x+1]
        self.quant-=1
    def inserir(self,valor):
        if self.quant != 5:
            self.lista[sel.quant+1]= valor
            self.quant+=1
    def getPrim(self):
        return self.lista[0]
    def estahvazia(self):
        return self.quant == 0
    def estahcheia(self):
        return self.quant == 5
    
