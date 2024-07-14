
def isOctal(x):
    sw = True
    while (x > 0) and sw:
        if x%10 > 7:
            sw = False
        x /= 10
    return sw

# print(isOctal(108));
        
        
def sumaRec(x):
    if x < 1:
        return x
    else:
        return x + sumaRec(x-1)
        

print(sumaRec(10))


