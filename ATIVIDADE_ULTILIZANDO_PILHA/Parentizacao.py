import PilhaD
p=PilhaD.PilhaD()
erro='(5+3))-2('
x=0
z=0
while z !='z':
    if erro[x]=='(':
        p.push(x)
    elif erro[x]==')':
        if p.estaVazia==False:
            p.pop()
        else:
            print('Erro fechamento sem abertura!')
            z='z'
    x+=1
if p.estaVazia is False:
    print('Erro abertura sem fechamento!')
