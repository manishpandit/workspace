import random

def is_sorted(a):
    for i in range(1, len(a)):
        if a[i-1] > a[i]:
            return False
    return True

def random_array(size):
    return random.sample(range(size * 10), size)
