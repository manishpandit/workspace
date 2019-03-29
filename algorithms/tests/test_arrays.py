from sequence import even_odd
import unittest

class TestArrays(unittest.TestCase):
    def test_even_odd(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8]
        print(a)
        even_odd.even_odd(a)
        print(a)
        self.assertTrue(self.validate_even_odd(a))
        
    def validate_even_odd(self, a):
        ''' returns true if even and odd numbers are separated 
        with even numbers first and odd numbers later.'''
        i = 0
        while i < len(a) and a[i] % 2 == 0:
            i += 1
        while i < len(a) and a[i] % 2 != 0:
            i += 1
        return i == len(a)

if __name__ == "__main__":
    unittest.main()