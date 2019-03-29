''' Implementation of selection sort '''

def selection_sort(a):
    for i in range(0, len(a)):
        min = i
        for j in range(i + 1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]




