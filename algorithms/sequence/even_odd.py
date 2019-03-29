def even_odd(a):
    ''' separates even and odd numbers in a sequence. '''
    i = -1
    for j in range(len(a)):
        if a[j] % 2 == 0:
            i += 1
            a[i], a[j] = a[j], a[i]

a = [1, 2, 3, 4, 5, 6, 7, 8]
print(a)
even_odd(a)
print(a)

