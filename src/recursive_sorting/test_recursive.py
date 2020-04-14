import unittest
import random
import copy
from recursive_sorting import (
    quick_sort,
    merge_sort,
    merge_sort_in_place,
)


class RecursiveSortingTests(unittest.TestCase):

    test_arrays = (
        lambda: [1, 5, 8, 4, 2, 9, 6, 0, 3, 7],
        lambda: [],
        lambda: [2],
        lambda: [-1, 0, 1, 2, 3, 4, 5],
        lambda: random.sample(range(200), 50),
    )

    def test_quick_sort(self):

        for test_array in self.test_arrays:

            arrayA = test_array()
            arrayB = copy.copy(arrayA)
            self.assertEqual(quick_sort(arrayA), sorted(arrayB))

    def test_merge_sort(self):

        for test_array in self.test_arrays:

            arrayA = test_array()
            arrayB = copy.copy(arrayA)
            self.assertEqual(merge_sort(arrayA), sorted(arrayB))

    def test_in_place_merge_sort(self):

        for test_array in self.test_arrays:

            arrayA = test_array()
            arrayB = copy.copy(arrayA)
            self.assertEqual(
                merge_sort_in_place(arrayA, 0, len(arrayA) - 1),
                sorted(arrayB),
            )


if __name__ == '__main__':
    unittest.main()
