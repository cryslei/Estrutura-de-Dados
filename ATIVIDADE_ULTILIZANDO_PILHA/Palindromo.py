import PilhaD
p=PilhaD.PilhaD()
y=input('Digite a palavra:')

for x in y:
    p.push(x)
i=0
while i<len(y)) and y[i]==p.getTopo():
    p.pop()
    i+=1
if p.estaVazia():
    print('É palindromo!')
else:
    print('Não é palindromo!')
