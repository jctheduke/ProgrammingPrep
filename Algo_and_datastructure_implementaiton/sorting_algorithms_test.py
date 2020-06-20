from random import sample
import unittest

from sorting_algorithms import quick_sort, bubble_sort, merge_sort, insertion_sort,selection_sort, heap_sort,bucket_sort,counting_sort,radix_sort, shell_sort



class TestSortingAlgorithms(unittest.TestCase):
    B = sample(range(0,1000),5)
    print(B)
    expected_result = sorted(B)
    
    def test_quicksort(self):
        test_result_quick = quick_sort(self.B.copy())
        self.assertEqual(self.expected_result, test_result_quick)
    
    def test_bubblesort(self):
        test_result = bubble_sort(self.B.copy())
        self.assertEqual(self.expected_result, test_result)
    
    def test_mergesort(self):
        test_result = merge_sort(self.B.copy())
        self.assertEqual(self.expected_result, test_result)
    
    def test_inserstion_sort(self):
        test_result = insertion_sort(self.B.copy())
        self.assertEqual(self.expected_result, test_result)
    
    def test_selection_sort(self):
        test_result = selection_sort(self.B.copy())
        self.assertEqual(self.expected_result, test_result)
    
    def test_heap_sort(self):
        test_result = heap_sort(self.B.copy())
        self.assertEqual(self.expected_result, test_result)

    def test_count_sort(self):
        test_result = counting_sort(self.B.copy())
        self.assertEqual(self.expected_result, test_result)

    # def test_bucket_sort(self):
    #     test_result = bucket_sort(self.B.copy())
    #     self.assertEqual(self.expected_result, test_result)

    def test_radix_sort(self):
        test_result = radix_sort(self.B.copy())
        self.assertEqual(self.expected_result, test_result)
    
    def test_shell_sort(self):
        test_result = shell_sort(self.B.copy())
        self.assertEqual(self.expected_result, test_result)

if __name__ == '__main__':
    unittest.main()
