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


def __quick_sort(array, i_left, i_right, compare=compare_ascending):

    #=======================================
    # RECURSIVE CASE: array can be partitioned

    # while length to be sorted is more than 1
    if i_left < i_right:
        # find a new partition
        i_middle = __quick_sort_partition(array, i_left, i_right, compare)
        # sort the left
        __quick_sort(array, i_left, i_middle - 1, compare)
        # sort the right
        __quick_sort(array, i_middle + 1, i_right, compare)

    #=======================================
    # BASE CASE: array cannot be partitioned

    return


def __quick_sort_partition(array, i_left, i_right, compare=compare_ascending):

    # choose a pivot value
    pivot = array[i_right]

    # move items less than pivot left, move items more than pivot right
    i = i_left
    for j in range(i_left, i_right):
        if compare(array[j], pivot) < 0:
            array[i], array[j] = array[j], array[i]
            i += 1

    # swap pivot to middle
    array[i], array[i_right] = array[i_right], array[i]

    return i


########################################
#   MERGE SORT
########################################


def merge_sort(array, compare=compare_ascending):

    return __merge_sort(array, compare)


def __merge_sort(array, compare=compare_ascending):

    #=======================================
    # BASE CASE: array cannot be split

    if len(array) <= 1:
        return array

    #=======================================
    # RECURSIVE CASE: array can be split

    left, right = __merge_sort__split(array)

    # sort each part
    left = __merge_sort(left, compare)
    right = __merge_sort(right, compare)

    # merge
    return __merge_sort__merge(left, right, compare)


def __merge_sort__split(array):

    halfish = len(array) // 2

    left = array[:halfish]
    right = array[halfish:]

    return (left, right)


def __merge_sort__merge(left, right, compare=compare_ascending):

    n_left = len(left)
    n_right = len(right)

    # create blank merged array
    n_merged = n_left + n_right
    merged = [None] * n_merged

    # merge left part and right part into merged array...

    i_merged, i_left, i_right = 0, 0, 0

    # while neither left part or right part is "empty"...
    while i_left < n_left and i_right < n_right:

        left_item = left[i_left]
        right_item = right[i_right]

        if compare(left_item, right_item) <= 0:
            # if equal, preserve current order: left, right
            merged[i_merged] = left_item
            i_left += 1

        else:
            merged[i_merged] = right_item
            i_right += 1

        i_merged += 1

    # one part will not be empty, so...
    if i_left < n_left:
        # merge rest of left
        merged[i_merged:] = left[i_left:]

    elif i_right < n_right:
        # merge rest of right
        merged[i_merged:] = right[i_right:]

    else:
        raise Exception("HOW DID YOU GET HERE?")

    return merged


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
