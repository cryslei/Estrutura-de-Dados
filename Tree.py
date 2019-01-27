class Tree:

    def __init__(self):
        self.raiz = None

    def retornaPai(self, valor):
        if self.raiz == None:
            return False
        
        elif self.raiz.info == valor:
            return None
        else:
            return self.raiz.retornaPai(valor)
        
    def contaDescendentes(self, valor):
         
        if self.raiz == None:
            return False
        else:
            return self.raiz.contaDescendentes(valor)
        
    def decresce(self):
        if self.raiz != None:
            self.raiz.decresce()
        else:
            return False

    def insere(self, valor):
        if self.raiz == None:
            self.raiz = No(valor)
        else:
            self.raiz.insere(valor)

    def busca(self, valor):
        if self.raiz == None:
            return False
        else:
            return self.raiz.busca(valor)
        
    def inOrdem(self):
        if self.raiz != None:
            self.raiz.inOrdem()

    def soma(self):
        if self.raiz != None:
            return self.raiz.soma()

    def somaFolhas(self):
        if self.raiz != None:
            return self.raiz.somaFolhas()
        
    def printFolhas(self):
        if self.raiz != None:
            self.raiz.printFolhas()
        
    def altura(self):
        if self.raiz != None:
            return self.raiz.altura()
        
    def h(self,valor):
        if self.raiz != None:
            return self.raiz.h(valor)
        
    def nivel(self, valor):
        if self.raiz != None:
            return self.raiz.nivel(valor)

    def maisdir(self):
        if self.raiz != None:
            return self.raiz.maisdir()

    
    def maisesq(self):
        if self.raiz != None:
            return self.raiz.maisesq()

    def NumPar(self):
        if self.raiz != None:
            self.raiz.NumPar()
    def NumImpar(self):
        if self.raiz != None:
            self.raiz.NumImpar()
            
    def posOrdem(self):
        if self.raiz != None:
            self.raiz.posOrdem()
            
    def preOrdem(self):
        if self.raiz != None:
            self.raiz.preOrdem()
            
    def preOrdemInverso(self):
        if self.raiz != None:
            self.raiz.preOrdemInverso()
            
    def estritamente(self):
        if(self.raiz != None):
            return self.raiz.estritamente()
        
    def imprimeOrdemAposDetRaiz(self,valor):
        if(self.raiz != None):
            return self.raiz.AposDetRaiz(valor)
        
    def hdir(self,valor):
        if self.raiz != None:
            return self.raiz.hdir(valor)
    def hesq(self,valor):
        if self.raiz != None:
            return self.raiz.hesq(valor)
    def hInOrdem(self,valor):
        if self.raiz != None:
            return self.raiz.hInOrdem(valor)
    def contNo(self):
        if self.raiz != None:
            return self.raiz.contNo()

    def possuiUmFilho(self):
        if self.raiz != None:
            self.raiz.possuiUmFilho()

    def maiorDeterminado(self, valor):
        if self.raiz != None:
            return self.raiz.maiorDeterminado(valor)

    def retornaIrmaoMenor(self):
        if self.raiz == None:
            return None
        else:
            return self.raiz.retornaIrmaoMenor()

    def retornaIrmaoMaior(self):
        if self.raiz == None:
            return None
        else:
            return self.raiz.retornaIrmaoMaior()

    def retornaIrmao(self):
        if self.raiz == None:
            return None
        else:
            return self.raiz.retornaIrmao()

    def ocorrencias(self, valor):
        if self.raiz == None:
            return 0
        else:
            return self.raiz.ocorrencias(valor)

    def retornaMenorImediato(self, valor):
        if valor == self.raiz.info:
            return False
        return self.raiz.retornaMenor(valor)
    def PrintDescendentes(self, valor):
        if valor != None:
            return self.raiz.PrintDescendentes(valor)
            

class No:
 
    def __init__(self, valor):
        self.info = valor
        self.esq = None
        self.dir = None
        self.cont = 0
    def decresce(self):
        if self.dir != None:
            self.dir.decresce()
        if self.info != None and (self.esq != None or self.dir != None):
            print(self.info,end=" ")
        if self.esq != None:
            self.esq.decresce()
            

    def contaDescendentes(self, valor):
        if valor == self.info:
            aux = aux1 = 0
            if self.esq != None:
                aux = self.esq.somaFilho()
            if self.dir != None:
                aux1 = self.dir.somaFilho()
            return (aux+aux1)
        elif valor <= self.info:
            if self.esq == None:
                return False
            else:
                return self.esq.contaDescendentes(valor)
        else:
            if self.dir == None:
                return False
            else:
                return self.dir.contaDescendentes(valor)

    def somaFilho(self):
        total = 1
        if self.esq != None:
            total += self.esq.somaFilho()
        if self.dir != None:
            total += self.dir.somaFilho()
        return total


    def retornaPai(self, valor): 
        if valor == self.info:
            
            return True
            
        elif valor < self.info:
            if self.esq == None:
                return False
            else:
                aux = self.esq.retornaPai(valor)
                if aux == True:
                    return self.info
                else:
                    if aux != False:
                        return aux
                    else:
                        return False
                    
        else:
            if self.dir == None:
                return False
            else:
                aux = self.dir.retornaPai(valor)
                if aux == True:
                    return self.info
                else:
                    if aux != False:
                        return aux
                    else:
                        return False
    

    def insere(self, valor):
        if valor <= self.info:
            if self.esq == None:
                self.esq = No(valor)
            else:
                self.esq.insere(valor)
        else:
            if self.dir == None:
                self.dir = No(valor)
            else:
                self.dir.insere(valor)

    def busca(self, valor):
        if valor == self.info:
            return True
        elif valor <= self.info:
            if self.esq == None:
                return False
            else:
                return self.esq.busca(valor)
        else:
            if self.dir == None:
                return False
            else:
                return self.dir.busca(valor)
    
    def inOrdem(self):
        if self.esq != None:
            self.esq.inOrdem()
        print(self.info,end=" ")
        if self.dir != None:
            self.dir.inOrdem()

    def soma(self):
        total = self.info
        if self.esq != None:
            total += self.esq.soma()
        if self.dir != None:
            total += self.dir.soma()
        return total

    def somaFolhas(self):
        total = 0
        if self.esq==None and self.dir == None:
            total = self.info
        if self.esq != None:
            total += self.esq.somaFolhas()
        if self.dir != None:
            total += self.dir.somaFolhas()
        return total
    
    def printFolhas(self):
        if self.esq != None:
            self.esq.printFolhas()
        if self.esq == None and self.dir == None:
            print(self.info,end=" ")
        if self.dir != None:
            self.dir.printFolhas()

    def max(self, a, b):
        if a>b:
            return a
        return b

    def altura(self):
        hesq=hdir=0
        if self.esq!=None:
            hesq=self.esq.altura()
        if self.dir!=None:
            hdir=self.dir.altura()
        return 1 + max(hesq,hdir)

    def h(self, valor):
        if valor == self.info:
            return self.altura()
        elif valor <= self.info:
            if self.esq == None:
                return False
            else:
                return self.esq.h(valor)
        else:
            if self.dir == None:
                return False
            else:
                return self.dir.h(valor)
 
    def nivel(self, valor):
        if valor == self.info:
             return 1
        elif valor <= self.info:
            if self.esq == None:
                return False
            else:
                aux = self.esq.nivel(valor)
                if aux != False:
                    return 1+aux
                else:
                    return False
        else:
            if self.dir == None:
                return False
            else:
                aux = self.dir.nivel(valor)
                if aux != False:
                    return 1+aux
                else:
                    return False

    def maisdir(self):
        if self.dir!=None:
            return self.dir.maisdir()
        else:
            return self.info

    def maisesq(self):
        if self.esq!=None:
            return self.esq.maisesq()
        else:
            return self.info

    def NumPar(self):
        if self.esq != None:
            self.esq.NumPar()
        if self.info%2 == 0:
            print(self.info, end=" ")
        if self.dir != None:
            self.dir.NumPar()

    def NumImpar(self):
        if self.esq != None:
            self.esq.NumImpar()
        if self.info%2 != 0:
            print(self.info, end=" ")
        if self.dir != None:
            self.dir.NumImpar()

    def posOrdem(self):
        if self.esq != None:
            self.esq.posOrdem()
        if self.dir != None:
            self.dir.posOrdem()
        if self.info != None:
            print(self.info,end=" ")
            
    def preOrdem(self):
        if self.info != None:
            print(self.info,end=" ")
        if self.esq != None:
            self.esq.posOrdem()
        if self.dir != None:
            self.dir.posOrdem()    
            
    def estritamente(self):
        if(self.esq == None and self.dir == None):
            return True
        if(self.esq == None and self.dir != None):
            return False
        if(self.esq != None and self.dir == None):
            return False
        if(self.esq != None and self.dir != None):
            aux = self.esq.estritamente();
            aux1 = self.dir.estritamente();
            if(aux == True and aux1 == True):
                return True
            else:
                return False
    def AposDetRaiz(self,valor):
        if valor == self.info:
            if self.dir != None:
                self.dir.inOrdem()
            return True
        elif valor < self.info:
            if self.esq == None:
                return False
            else:
                aux = self.esq.AposDetRaiz(valor)
                if aux == True and self.dir != None:
                    print(self.info)
                    self.dir.inOrdem()
                return True
        else:
            if self.dir == None:
                return False
            else:
                return self.dir.AposDetRaiz(valor)
    def hdir(self, valor):
        if valor == self.info:
            return self.maisdir()
        elif valor <= self.info:
            if self.esq == None:
                return False
            else:
                return self.esq.hdir(valor)
        else:
            if self.dir == None:
                return False
            else:
                return self.dir.hdir(valor)
    def hesq(self, valor):
        if valor == self.info:
            return self.maisesq()
        elif valor <= self.info:
            if self.esq == None:
                return False
            else:
                return self.esq.hesq(valor)
        else:
            if self.dir == None:
                return False
            else:
                return self.dir.hesq(valor)
    def preOrdemInverso(self):
        if self.info != None:
            print(self.info,end=" ")
        if self.dir != None:
            self.dir.posOrdem()  
        if self.esq != None:
            self.esq.posOrdem()
            
    def hInOrdem(self, valor):
        if valor == self.info:
            return self.inOrdem()
        elif valor <= self.info:
            if self.esq == None:
                return False
            else:
                return self.esq.hInOrdem(valor)
        else:
            if self.dir == None:
                return False
            else:
                return self.dir.hInOrdem(valor)
    def contNo(self):
        no = 1
        if self.esq != None:
            no+=self.esq.contNo()
        if self.dir != None:
            no+=self.dir.contNo()
        return no
    def possuiUmFilho(self):
        if self.esq != None:
            self.esq.possuiUmFilho()
        if self.info != None and (self.esq != None or self.dir != None):
            print(self.info,end=" ")
        if self.dir != None:
            self.dir.possuiUmFilho()

    def maiorDeterminado(self, valor):
        if valor == self.info:
            if self.dir != None:
                self.dir.inOrdem()
            return True
        elif valor <= self.info:
            if self.esq == None:
                return False
            else:
                aux = self.esq.maiorDeterminado(valor)
                if aux == True and self.dir != None:
                    print(self.info)
                    self.dir.inOrdem()
                return True
        else:
            if self.dir == None:
                return False
            else:
                return self.dir.AposDetRaiz(valor)

    def retornaIrmaoMenor(self):
        if self.esq!=None:
            aux = self.esq.retornaIrmaoMenor()
            if aux == True and self.dir!=None:  # se aux é True é porque a volta recursiva veio do cara mais a esquerda
                                                # logo, tenho que retornar a info do cara da direita (que só existe
                                                # se dir for diferente de None, por isso o AND)

                return self.dir.info  
            else: # se aux é diferente de True é porque já estou retornando o irmão da direita oo None se não tinha irmão
                if self.dir==None: # se não tem irmão retorna None
                    return None
                else:
                    return aux  # se tiver irmão, continua retornando ele. 
        else:
            return True # retorna True quando chega no no cara mais a esquerda, ou seja, no menor

    def retornaIrmaoMaior(self):
        if self.dir !=None:
            aux = self.dir.retornaIrmaoMaior()
            if aux == True and self.esq!=None:  # se aux é True é porque a volta recursiva veio do cara mais a esquerda
                                                # logo, tenho que retornar a info do cara da direita (que só existe
                                                # se dir for diferente de None, por isso o AND)

                return self.esq.info  
            else: # se aux é diferente de True é porque já estou retornando o irmão da direita oo None se não tinha irmão
                if self.esq == None: # se não tem irmão retorna None
                    return None
                else:
                    return aux  # se tiver irmão, continua retornando ele. 
        else:
            return True # retorna True quando chega no no cara mais a esquerda, ou seja, no menor
        



    def ocorrencias(self,x):
        if x == self.info:
            if self.esq!=None: 
                return 1 + self.esq.ocorrencias(x)
            else:
                return 1
        elif x < self.info:
            if self.esq!=None:
                return self.esq.ocorrencias(x)
            else:
                return 0
        else:
            if self.dir!=None:
                return self.dir.ocorrencias(x)
            else:
                return 0

    def retornaIrmao(self, valor):
        if self.esq != None and self.esq.info == valor and self.dir != None:
            return self.dir.info 
        
        elif self.dir != None and self.dir.info == valor and self.esq != None:
            return self.esq.info
            
        else:
            if valor <= self.info:
                if self.esq != None:
                    aux = self.esq.retornaIrmao(valor)
                    return aux
                else:
                    return False
            else:
                if self.dir != None:
                    aux = self.dir.retornaIrmao(valor)
                    return aux
                else:
                    return False

    def retornaMenorImediato(self, valor):
        if valor == self.info:
            return self.info

        elif valor <= self.info:
            if self.esq != None:
                aux = self.esq.retornaMenorImediato(valor)
                if aux > self.info:
                    return self.info
                else:
                    return aux
            else:
                return False

        else:
            if self.dir != None:
                aux = self.dir.retornaMenorImediato(valor)
                if aux > self.info:
                    return self.info
                else:
                    return aux
            else:
                return False


a = Tree()
a.insere(4)
a.insere(2)
a.insere(1)
a.insere(3)
a.insere(6)
a.insere(5)
a.insere(7)

a.hInOrdem(4)
##a.possuiUmFilho()
##a.maiorDeterminado(4)
##a.decresce()
##print(a.estritamente())
##print(a.contNo())
##print(a.retornaPai(4))
##print(a.maisdir())
##a.NumImpar()
##a.NumPar()
##print(a.nivel(8))
##print(a.h(5))  encontra o valor e ver qual a altura dessa arvore
##a.printFolhas()
##print(a.altura())
##print(a.hdir(3))
##a.preOrdem()
##a.hInOrdem(7)
