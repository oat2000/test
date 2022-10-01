from insert_sort_code.insert_sort import insertion_sort

import unittest

class Test(unittest.TestCase):
    def test_decimal(self):
        data = [0.3,0.2,0.1]
        test_true = [0.1,0.2,0.3]
        result = insertion_sort(data)
        self.assertEqual(result,test_true)
    
    def test_positive_negative(self):
        data = [-1,-2,-3,1,2,3]
        test_true = [-3,-2,-1,1,2,3]
        result = insertion_sort(data)
        self.assertEqual(result,test_true)
    
    def test_1000(self):
        data = [-1000,1000,-100,100]
        test_true = [-1000,-100,100,1000]
        result = insertion_sort(data)
        self.assertEqual(result,test_true)

    def test_answer(self):
        data = [15, 16, 2, 8, 50, 35]
        test_true = [2,8,15,16,35,50]
        result = insertion_sort(data)
        self.assertEqual(result,test_true)