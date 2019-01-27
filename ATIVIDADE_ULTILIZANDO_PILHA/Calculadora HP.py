import PilhaD
p=PilhaD.PilhaD()

conta='4 3 5 2 - + *'
sinais=['+','-','*','/']

for i in range(len(conta)):
    if conta[i] not in sinais:
        p.push(conta[i])
    else:
        op2=int(p.getTopo())
        p.pop()
        op1=int(p.getTopo())
        p.pop
        if conta[i]=='+':
            p.push(op1+op2)
        elif conta[i]=='-':
            p.push(op1-op2)
        elif conta[i]=='*':
            p.push(op1*op2)
        else:
            p.push(op1/op2)

print(p.getTopo())
