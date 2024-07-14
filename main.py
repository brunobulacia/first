
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
        

# print(sumaRec(10))

def sumarFrac(n):
    s = 0
    c = n
    for i in range(1, n+1):
        s += c/i
        c -= 1
    return s

# print(sumarFrac(4))


def sumarDig(x):
    s = 0
    if x < 9:
        s = x
    else:
        s = x%10 + sumarDig(x//10)
    return s

def cadenaInv(x):
    if x == "":
        return x
    else:
        return x[len(x)-1] + cadenaInv(x[:len(x)-1])

def swap(x, y):
    aux = x
    x = y
    y = aux


def moveGreatest(x):
    for i in range(0, len(x)-1):
        if x[i] > x[i+1]:
            swap(x[i], x[i+1])
    return x
l = [1,2,9,4]

print(moveGreatest(l))



