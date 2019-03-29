import random

def merge(a, start, mid, end):
    ''' Merge two subsets of the sorted sequences to form 
        a completely sorted sequence.
        Arguments:
        :param a: a sequence to be sorted.
        :param start: starting index of the first sub-sequence.
        :param mid: mid - 1 is the last elements of the first sub-sequence and
        :param mid is the first element of the second sub-sequence.
        :param end: index of last last element + 1
    '''
    i, j, k = 0, 0, start
    L = a[start:mid]
    R = a[mid:end]
    for k in range(start, end):
        if j >= len(R) or (i < len(L) and L[i] < R[j]):
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
    
def sort(a, start, end):
    ''' Implementation of merge sort algorithm.
        Arguments:
        :param a: a sequence defined by start and end; to be sorted in-place.
        :param start: index of first element.
        :param end: last element's index + 1
    '''

    if end - start < 2:
        return
    mid = (end - start) // 2 + start
    sort(a, start, mid)
    sort(a, mid, end)
    return merge(a, start, mid, end)

def merge_sort(a):
    ''' Implementation of merge sort algorithm.
        Arguments:
        :param a: a sequence defined by start and end; to be sorted in-place.
    '''
    return sort(a, 0, len(a))

