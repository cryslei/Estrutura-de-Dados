class Pilha():
    def __init__(self):
        self.lista = [None,None,None,None,None]
        self.quant = 0
    def push(self,valor):
        if self.quant < 5:
            self.lista[self.quant]= valor
            self.quant+=1       
    def pop(self):
        if self.quant > 0:
            self.quant-=1
    def show(self):#usar __dict__ na minha opniao
        for x in range(self.quant):    
            print(self.lista[x])
    def getTopo(self):
        return self.lista[self.quant]
    def estahvazia(self):
        return self.quant == 0
    def estahcheia(self):
        return self.quant == 5
