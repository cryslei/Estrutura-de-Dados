class No():
    def __init__(self,valor,proximo):
        self.info=valor
        self.prox=proximo

class PilhaD():
    def __init__(self):
        self.prim=None
        self.ult=None
        self.quant=0

    def push(self,valor):#inserirInicio
        if self.quant==0:
            self.prim=self.ult=No(valor,None)
        else:
            self.prim=No(valor,self.prim)
        self.quant+=1

    def pop(self):#remover
        if self.quant==1:
            self.prim=self.ult=None
        else:
            self.prim=self.prim.prox
        self.quant-=1

    def getTopo(self):
        return self.prim.info

    def estaVazia(self):
        return self.quant==0
