def mezcla(x, i, mid, j):
    k = i
    l = mid
    p = mid + 1
    s = j
    aux = []
    while (k <= l) and (p <= s):
        if (x[k] > x[p]):
            aux.append(x[p])
            p += 1
        else:
            aux.append(x[k])
            k += 1
    while (k <= l):
        aux.append(x[k])
        k += 1
    while (p <= s):
        aux.append(x[p])
        p += 1
    for k in range(i, j+1):
        del x[i]
    for n in range(0, len(aux)):
        x.append(aux[n])


def merge_sort(x, i, j):
    if i < j:
        mid = (i+j)//2
        merge_sort(x, i, mid)
        merge_sort(x, mid+1, j)
        mezcla(x, i, mid, j)


x = [9, 2, 11, 10, 15, 0, 5, 6]
merge_sort(x, 0, len(x)-1)
print(x)
