import random as r


def pivotear(v, i, j):
    aux = v[j]
    k = i-1
    while i < j:
        if v[i] < aux:
            k += 1
            temp = v[k]
            v[k] = v[i]
            v[i] = temp
        i += 1
    k += 1
    temp = v[k]
    v[k] = v[i]
    v[i] = temp
    v.append(k)
    return v


# print(pivotear(v, 0, len(v)-1))
# pivotear(v, 0, len(v)-1)
# print(v)


def quick_sort(v, i, j):
    aux = v[j]
    k = i-1
    p = i
    while p < j:
        if v[p] < aux:
            k += 1
            temp = v[k]
            v[k] = v[p]
            v[p] = temp
        p += 1
    k += 1
    temp = v[k]
    v[k] = v[p]
    v[p] = temp
    if i < j:
        v = quick_sort(v, i, k-1)
        v = quick_sort(v, k+1, j)
    return v


def PivotearCrj(v, start, end):
    pivot = v[end]
    i = start - 1
    for j in range(start, end):
        if v[j] < pivot:
            i += 1
            temp = v[i]
            v[i] = v[j]
            v[j] = temp
    i += 1
    temp = v[i]
    v[i] = v[end]
    v[end] = temp
    return i


def QuickSort(v, start, end):
    if (end <= start):
        return
    pivot = PivotearCrj(v, start, end)
    v = QuickSort(v, start, pivot-1)
    v = quick_sort(v, pivot+1, end)
    return v


v = []
for i in range(0, 8):
    v.append(r.randint(0, 13))
# v = [8, 0, 3, 3, 8, 0, 1, 4]
print(v)

print(QuickSort(v, 0, len(v)-1))
