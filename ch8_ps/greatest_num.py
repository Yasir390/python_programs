
def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    

a =20
b = 23
c = 21    

print("greatest number is : ",greatest(a,b,c))