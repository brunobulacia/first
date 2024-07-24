import random as r


def swap(v, i, j):
    a = v[i]
    b = v[j]
    v.pop(i)
    v.pop(j-1)
    v.insert(i, b)
    v.insert(j, a)


def bubble(v):
    for i in range(0, len(v)):
        for j in range(0, len(v)-i-1):
            if v[j] > v[j+1]:
                swap(v, j, j+1)


def shell_sort(v):
    f = len(v) // 2
    while f > 0:
        sw = True
        for i in range(0, len(v)-f):
            if v[i] > v[f+i]:
                swap(v, i, f+i)
                sw = False
        if sw:
            f = f // 2


def changer(v, i, f, sw):
    if i < len(v)-f:
        if v[i] > v[f+i]:
            swap(v, i, f+i)
            sw = False
        changer(v, i+1, f, sw)
    return sw


def shell_rec(v, f):
    if f > 0:
        sw = changer(v, 0, f, True)
        if sw:
            f = f // 2
        shell_rec(v, f)


v = [3, 2, 1, 9, 0, 99, 99, 1]
# print(changer(v, 0, len(v)//2, True))
shell_rec(v, len(v)//2)


print(v)
