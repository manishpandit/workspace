def parent(i):
    return (i - 1) // 2

def left(i):
    return (i * 2) + 1

def right(i):
    return (i * 2) + 2

def max_heapify(a, n, i):
    l = left(i)
    r = right(i)
    largest = i
    if l < n and a[l] > a[i]:
        largest = l
    if r < n and a[r] > a[largest]:
        largest = r
    if i != largest:
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, n, largest)

def build_max_heap(a):
    for i in range(len(a) // 2, -1, -1):
        max_heapify(a, len(a), i)

def heap_sort(a):
    build_max_heap(a)
    for i in range(len(a) - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        max_heapify(a, i, 0)


 