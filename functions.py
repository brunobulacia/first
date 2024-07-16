import math

# vowels = ['a', 'e', 'i', 'o', 'u']


# def isOctal(x):
#     sw = True
#     while (x > 0) and sw:
#         if x%10 > 7:
#             sw = False
#         x /= 10
#     return sw

# # print(isOctal(108));
        
        
# def sumaRec(x):
#     if x < 1:
#         return x
#     else:
#         return x + sumaRec(x-1)
        

# def sumarFrac(n):
#     s = 0
#     c = n
#     for i in range(1, n+1):
#         s += c/i
#         c -= 1
#     return s


# def sumarDig(x):
#     s = 0
#     if x < 9:
#         s = x
#     else:
#         s = x%10 + sumarDig(x//10)
#     return s

# def cadenaInv(x):
#     if x == "":
#         return x
#     else:
#         return x[len(x)-1] + cadenaInv(x[:len(x)-1])




# def fibo(x):
#     f = 0
#     if x < 2:
#         f = x
#     else:
#         f = fibo(x-1) + fibo(x-2)
#     return f

# def factorial(x):
#     f = 0;
#     if x < 2:
#         f = x
#     else:
#         f = x*factorial(x-1)
#     return f

# def pertenece(x):
#     i = 1;
#     while x > fibo(i):
#         i += 1
#     return x == fibo(i)

# def cut(x, i):
#     return x[:i] + x[i+1:len(x)]

# def borraVocales(x):
#     if len(x) > 0:
#         if (x[:len(x)-1] in vowels):
#             cut(x,len(x)-1)
#     return x

# def borrarPrimero(x):
#     x.remove("hola")
    
# def bubbleSort(x):
#     for i in range(0, len(x)-1):
#         for j in range(0, len(x)-i-1):
#             if (x[j] > x[j+1]):
#                 aux = x[j]
#                 x[j] = x[j+1]
#                 x[j+1] = aux
#     return x
        
# def move(x, n):
#     if n > 1:
#         x = move(x, n-1)
#         if x[n-2] > x[n-1]:
#             aux = x[n-2]
#             x[n-2] = x[n-1]
#             x[n-1] = aux
#     return x 


# def bSort(x, n):
#     if n > 0:
#         x = bSort(x, n-1)
#         x = move(x, n)
#     return x


# # PROCESO PARA ELIMINAR LOS DIGITOS PARES DE UN NUMERO
# # PROCESO PARA ELIMINAR UN DIGITO DE UN NUMERO DADA UNA POSICION
# # 3164,2 ---> 314
# # 3695,4 ---> 695

# def delDigit(x, n):
#     k = 10 ** (n-1)
#     r = (x % k)
#     x = ((x // k) // 10) * k + r
#     return x

# def borrarPares(x):
#     if x < 10:
#         if x%2 == 0:
#             x = 0
#     else:
#         d = x % 10
#         x //= 10
#         x = borrarPares(x)
#         if d%2 != 0:
#             x = x * 10 + d
#     return x

def inverso(x):
    if x > 9:
        d = x % 10
        x = x//10
        x = inverso(x)
        k = 10 ** (math.floor(math.log10(x))+1)
        x = d * k + x 
    return x

def isSorted(x):
    if x > 9:
        if (x %10 >= (x%100)//10):
            return False
        x //= 10
        x = isSorted(x)
    return True

def isPalin(x):
    if x != "":
        if (x[0] != x[len(x)-1]):
            return False
        x = x[1:len(x)-1]
        x = isPalin(x)
    return True