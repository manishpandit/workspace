def partition(a, p, r):
    # all the elements left of variable i 
    # are less than pivot.
    # start with one minus first element.
    i = p - 1
    # variable j runs from first element to one 
    # minus last. Last one is pivot.
    for j in range(p, r):
        # if current element is less than pivot
        # increment i and swap the current value with a[i].
        if a[j] <= a[r]:
            i += 1
            a[i], a[j] = a[j], a[i]
    # increment i and swap with pivot
    i += 1
    a[i], a[r] = a[r], a[i]
    # return the position of the pivot
    return i     

# recursive qsort method
# a : sequence to be sorted.
# p : points to the first element of the sequence.
# q : points to the last element of the sequence.
def qsort(a, p, r):
    # if there are no elements or just one element,
    # the sequence is already sorted.
    if p >= r:
        return
    # partition the sequence and get the pivot position
    q = partition(a, p, r)
    # sort all the elements before pivot
    qsort(a, p, q - 1)
    # sort all the elements after pivot
    qsort(a, q + 1, r)

def quick_sort(a):
    qsort(a, 0, len(a) - 1)
