"""
This is a pure python implementation of the insertion sort algorithm
For doctests run following command:
python -m unittest -v tests.test_insertion_sort
For manual testing run:
python insertion_sort.py
"""

def insertion_sort(a):
    ''' Implementation of insertion sort
        :param a: some mutable ordered collection with heterogeneous
        comparable items inside
        :return: the same collection ordered by ascending
        Examples:
        >>> insertion_sort([0, 5, 3, 2, 2])
        [0, 2, 2, 3, 5]
        >>> insertion_sort([])
        []
        >>> insertion_sort([-2, -5, -45])
        [-45, -5, -2]
    '''

    # starting with second element to end
    for i in range(1, len(a)):
        # save the key
        key = a[i]
        # starting with previous element, find the correct spot for
        # next element
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        # copy the key
        a[j+1] = key
