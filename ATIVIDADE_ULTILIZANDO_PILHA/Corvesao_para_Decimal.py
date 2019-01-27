import Pilha_Dinamica
p = Pilha_Dinamica.Pilha_Dinamica()
num = input('Numero para converte:')
base = int(input('Base da conversão:'))
aux = ['A', 'B', 'C', 'D', 'E', 'F']
i = 0
x = 0
while i<len(str(num)):
    if num[i] in aux:
        if base==16:
            pass
        else:
            print('Esse numero não pertece a essa base!!!')
            i = len(num)
            x = 1
    else:
        if int(num[i])>=base:
            print('Esse numero não pertece a essa base!!!')
            i = len(num)
            x = 1
    i+=1
if x<1:
    for j in num:
        if base==16:
            if j=='A':
                p.push('10')
            elif j=='B':
                p.push('11')
            elif j=='C':
                p.push('12')
            elif j=='D':
                p.push('13')
            elif j=='E':
                p.push('14')
            elif j=='F':
                p.push('15')
            else:
                p.push(j)
        else:
            p.push(j)
    resul = 0
    for j in range(len(num)):
        resul+=int(p.getPrim())*(base**j)
        p.pop()
    p.push(resul)
    p.show()
