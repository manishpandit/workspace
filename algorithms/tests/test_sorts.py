from sort import selection_sort, bubble_sort, insertion_sort
from sort import merge_sort, heap_sort, quick_sort, quick_sort2
from tests.utils import is_sorted, random_array
import unittest
import time

class TestSorts(unittest.TestCase):

    def test_sorts(self):
        
        sort_methods = [insertion_sort.insertion_sort,
            selection_sort.selection_sort,
            bubble_sort.bubble_sort,
            merge_sort.merge_sort,
            heap_sort.heap_sort,
            quick_sort.quick_sort,
            quick_sort2.quick_sort]
        size = [1, 2, 10, 1000, 10000]        
        
        for sort_method in sort_methods:
            print(sort_method.__name__)
            start = time.time()
            for i in size:
                print("testing size: ", i)
                a = random_array(i)
                sort_method(a)
                self.assertTrue(is_sorted(a))
            end = time.time()
            print("time: %.2f sec" % (end - start))

    

if __name__ == "__main__":
    unittest.main()