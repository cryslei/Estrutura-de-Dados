import PilhaD
p=PilhaD.PilhaD()
num=int(input('Numero:'))
base=int(input('Base:'))
while num>=base:
    p.push(num%base)
    num=num//base
p.push(num)
while not p.estaVazia():
    print(p.getTopo(),end='')
    p.pop()
