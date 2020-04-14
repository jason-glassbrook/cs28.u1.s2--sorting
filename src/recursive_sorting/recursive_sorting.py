############################################################
#   RECURSIVE SORTING
#-----------------------------------------------------------
#   GUIDED
#   - [ ] complete quick_sort()
#
#   MVP
#   - [ ] complete merge()
#   - [ ] complete merge_sort()
#
#   STRETCH
#   - [ ] complete merge_in_place()
#   - [ ] complete merge_sort_in_place()
#   - [ ] complete tim_sort()
############################################################

import sys
sys.path.append("../")

from compare import compare_ascending

########################################
#   QUICK SORT
########################################


def quick_sort(array, compare=compare_ascending):
    # TODO: guided

    return array


def merge(arrayA, arrayB, compare=compare_ascending):
    elements = len(arrayA) + len(arrayB)
    merged_array = [0] * elements
    # TODO: mvp

########################################
#   MERGE SORT
########################################


def merge_sort(array, compare=compare_ascending):
    # TODO: mvp

    return array


########################################
#   MERGE SORT - IN PLACE
########################################
#   STRETCH: implement an in-place merge sort algorithm


def merge_in_place(array, start, mid, end, compare=compare_ascending):
    # TODO: stretch

    return array


def merge_sort_in_place(array, l, r, compare=compare_ascending):
    # TODO: stretch

    return array


########################################
#   TIM SORT
########################################
#   STRETCH: implement the Timsort function below
#   hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt


def tim_sort(array, compare=compare_ascending):
    # TODO: stretch

    return array
