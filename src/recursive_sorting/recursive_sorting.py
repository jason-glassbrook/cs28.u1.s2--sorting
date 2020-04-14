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

    __quick_sort(array, 0, len(array) - 1, compare)

    return array


def __quick_sort(array, left, right, compare=compare_ascending):

    #=======================================
    # RECURSIVE CASE: array can be partitioned

    # while length to be sorted is more than 1
    if left < right:
        # find a new partition
        middle = __quick_sort_partition(array, left, right, compare)
        # sort the left
        __quick_sort(array, left, middle - 1, compare)
        # sort the right
        __quick_sort(array, middle + 1, right, compare)

    #=======================================
    # BASE CASE: array cannot be partitioned

    return


def __quick_sort_partition(array, left, right, compare=compare_ascending):

    # choose a pivot value
    pivot = array[right]

    # move items less than pivot left, move items more than pivot right
    i = left
    for j in range(left, right):
        if compare(array[j], pivot) < 0:
            array[i], array[j] = array[j], array[i]
            i += 1

    # swap pivot to middle
    array[i], array[right] = array[right], array[i]

    return i


########################################
#   MERGE SORT
########################################


def merge_sort(array, compare=compare_ascending):

    __merge_sort(array, compare)

    return array


def __merge_sort(array, compare=compare_ascending):

    #=======================================
    # BASE CASE: array cannot be split

    if len(array) <= 1:
        return array

    #=======================================
    # RECURSIVE CASE: array can be split

    left_part, right_part = __merge_sort__split(array)

    # sort each part
    left_part = __merge_sort(left_part, compare)
    right_part = __merge_sort(right_part, compare)

    # merge
    return __merge_sort__merge(left_part, right_part, compare)


def __merge_sort__split(array):

    halfish = len(array) // 2

    left_part = array[:halfish]
    right_part = array[halfish:]

    return (left_part, right_part)


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
