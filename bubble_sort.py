import math

# # COUNT THE DISTINCT ELEMENTS OF AN ARRAY
# x = [[4, 3, 2, 1, 0], [0, 4, 3, 2, 1], [
#     0, 0, 4, 3, 2], [0, 0, 0, 4, 3], [0, 0, 0, 0, 4]]


# def countDiff(x):
#     s = []
#     for i in range(0, len(x)):
#         if x[i] not in s:
#             s.append(x[i])
#     return len(s)


# def cargar(m):
#     for i in range(0, 5):
#         m.append([])
#         for j in range(0, 5):
#             m[i].append((i+1)*(j+1))


# def v(x, n, e):
#     if n > 0:
#         v(x, n-1, e+1)
#         x.append(e)


# a = []
# v(a,5, 0)

# print(a)
'''CARGAR UN VECTOR CON LOS DIGITOS DE UN NUMERO'''


# def cargarV(v, n):
#     if n > 0:
#         cargarV(v, n//100)
#         v.append(n % 100)


# v = []
# n = 123

# cargarV(v, n)

# print(v)

def inverso(x):
    if x > 9:
        d = x % 10
        x = x//10
        x = inverso(x)
        k = 10 ** (math.floor(math.log10(x))+1)
        x = d * k + x
    return x


def cargarS(v, n):
    if n > 0:
        return cargarS(v, n-1) + str(inverso(v[n-1]))
    return ""


def is_sorted(x):
    if x < 10:
        return True
    else:
        return is_sorted(x // 10) and ((x//10) % 10) < (x % 10)


# v = [4, 23, 54, 2, 4]
# print(cargarS(v, len(v)))

x = 65432
print(is_sorted(x))
