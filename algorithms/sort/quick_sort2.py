# partition the sequence and return the pivot point
def partition(a, p, r):    
    # pick the first element as pivot
    # set the left marker one past first element.
    # set right marker at the last element.
    pivot = a[p]
    left = p + 1
    right = r    

    while True:
        # keep 'left' moving right as long as values are less than
        # pivot and it doesn't cross over 'right'
        while left <= right and a[left] <= pivot:
            left += 1
        # keep 'right' moving left as long as values are greater than
        # pivot and it doesn't cross over 'left'
        while left <= right and a[right] >= pivot:
            right -= 1
        # if the left and right has not crossed over than
        # swap their values and repeat the whole process.
        if left <= right:
            a[left], a[right] = a[right], a[left]
        else:
            # if there is a cross over we are done.
            break
    # finally swap the pivot with right and return right
    a[p], a[right] = a[right], a[p]
    return right

def qsort(a, p, r):
    # if there is only one or no element, we are done.
    if p >= r:
        return
    # partition the sequence and find pivot
    q = partition(a, p, r)
    # sort elements left of pivot
    qsort(a, p, q - 1)
    # sort elements right of pivot
    qsort(a, q + 1, r)

def quick_sort(a):
    qsort(a, 0, len(a) - 1)  