"""
Problem: Sorting the array using QuickSort Algorithm
Input: An array of n numbers, in arbitrary order.
Output: An array of the same numbers, sorted from smallest-largest

* Reason of using:
- Run in place: operates on the input array only through repeated swaps of pairs of elements, and for this reason needs to allocate only a minuscule amount of additional memory for intermediate computations.
- Remarkably beautiful algorithm
"""

"""
Key idea: partition array around a pivot element

* Rearrange the array so that:
- left of pivot => less than pivot
- right of pivot => greater than pivot

* Note: put pivot in its "rightful position"
"""

from typing import List
import random
from copy import deepcopy

random.seed(2024)


def sort(input_path: str):
    with open(input_path, 'r') as f:
        data = [int(l) for l in f.readlines()]
        n = len(data)
    # print(f"Before sort: {data}")

    temp_data = deepcopy(data)
    cnt_dict = {}

    for way in ['left', 'right', 'median', 'random']:

        cnt_dict[way] = quick_sort(temp_data, 0, n-1, way)
        temp_data = deepcopy(data)

    return [cnt_dict['left'], cnt_dict['right'], cnt_dict['median']]


def quick_sort(arr: List[int], l: int, r: int, way: str):
    """
    Quick sort implementation of n-element array

    Parameters
    ----------
    arr : List[int]
        The array of integers
    l : int
        The left end-point
    r : int
        The right end-point
    """
    if l >= r:
        return 0

    p = choose_pivot(arr, l, r, way) # Choose the pivot position
    arr[l], arr[p] = arr[p], arr[l] # make pivot first
    j, cnt = partition(arr, l, r) # new pivot position -- correct one

    left_cnt = quick_sort(arr, l, j-1, way) # recursive on first-part
    right_cnt = quick_sort(arr, j+1, r, way) # recursive on second-part
    return cnt + left_cnt + right_cnt


def choose_pivot(arr: List[int], l: int, r: int, way: str):
    """
    Choose the pivot position in the array with left and right end-points

    Parameters
    ----------
    arr : List[int]
        The array of integers
    l : int
        The left end-point
    r : int
        The right end-point
    """
    way_dict = {
        'left': l, # left-most pivot
        'right': r, # right-most pivot
        'median': choose_median(arr, l, r), # median of 3
        'random': random.randint(l, r)
    }
    # return l # Left-most pivot
    # return r # Right-most pivot
    # return choose_median(arr, l, r) # median of 3
    # return random.randint(l, r) # Uniform-random pivot

    return way_dict[way]


def choose_median(arr: List[int], l: int, r: int):
    if r == l:
        return l
    mid = (r-l+1)//2 + l if (r-l+1) % 2 else (r-l+1)//2 + l - 1
    candidates = [arr[l], arr[r], arr[mid]]
    candidates.sort()
    median = l

    if arr[mid] == candidates[1]:
        median = mid
    elif arr[r] == candidates[1]:
        median = r

    return median


def partition(arr: List[int], l: int, r: int):
    """
    Rearrange the array around pivot

    Parameters
    ----------
    arr : List[int]
        The array of integers
    l : int
        The left end-point
    r : int
        The right end-point
    """
    p = arr[l]
    i = l+1
    cnt = 0
    for j in range(l+1, r+1):
        cnt += 1
        if arr[j] < p:
            arr[i], arr[j] = arr[j], arr[i] # swap i, j
            i += 1 # move up left-side pivot
    arr[l], arr[i-1] = arr[i-1], arr[l] # place pivot at correct position

    return i-1, cnt # report final pivot position


if __name__ == "__main__":
    sort('testCases/course1/assignment3Quicksort/input_coursera_01_100000.txt')


