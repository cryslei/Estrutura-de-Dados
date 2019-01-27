class No():
    def __init__(self,valor,proximo):
        self.info=valor
        self.prox=proximo

class FilaD():
    def __init__(self):
        self.prim=None
        self.ult=None
        self.quant=0

    def inserir(self,valor):#Fim
        if self.quant==0:
            self.prim=self.ult=No(valor,None)
        else:
            self.ult.prox=self.ult=No(valor,None) #faz diferença a posição do ult e ult.prox
        self.quant+=1
    
    def remover(self):#Inicio
        if self.quant==1:
            self.prim=self.ult=None
        else:
            self.prim=self.prim.prox
        self.quant-=1

    def getPrim(self):
        return self.prim.info

    def estaVazia(self):
        return self.quant==0

    def show(self):
        aux=self.prim
        while aux!=None:
            print(aux.info,end='')
            aux=aux.prox
