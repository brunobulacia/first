vowels = ['a', 'e', 'i', 'o', 'u']


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
        

def sumarFrac(n):
    s = 0
    c = n
    for i in range(1, n+1):
        s += c/i
        c -= 1
    return s


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


def moveGreatest(x):
    for i in range(0, len(x)-1):
        if x[i] > x[i+1]:
            aux = x[i]
            x[i] = x[i+1]
            x[i+1] = aux
    return x

def bubbleSort(x):
    for i in range(0, len(x)):
        x = moveGreatest(x)
    return x


# RECURSIVE BUBBLESORT
def moveGreat(x):
    if len(x) > 1:
        a = x[len(x)-1]
        x = moveGreat(x[:len(x)-1])
        x.append(a)
        if x[len(x)-2] > x[len(x)-1]:
            aux = x[len(x)-1]
            x[len(x)-1] = x[len(x)-2]
            x[len(x)-2] = aux
    return x


def fibo(x):
    f = 0
    if x < 2:
        f = x
    else:
        f = fibo(x-1) + fibo(x-2)
    return f

def factorial(x):
    f = 0;
    if x < 2:
        f = x
    else:
        f = x*factorial(x-1)
    return f

def pertenece(x):
    i = 1;
    while x > fibo(i):
        i += 1
    return x == fibo(i)

def cut(x, i):
    return x[:i] + x[i+1:len(x)]

def borraVocales(x):
    if len(x) > 0:
        if (x[:len(x)-1] in vowels):
            cut(x,len(x)-1)
    return x

def borrarPrimero(x):
    x.remove("hola")
        