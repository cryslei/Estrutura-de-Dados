#conversão
def conv(n,b):
    if n<b:
        return str(n)
    else:
        return conv(n//b,b)+str(n%b)
    
print(conv(10,2))
