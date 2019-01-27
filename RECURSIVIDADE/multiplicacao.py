#mutiplicação
def mult(x,y):
    if x==1:
        return y
    elif x==0:
        return 0
    else:
        return y+mult(x-1,y)

print(mult(5,4))
