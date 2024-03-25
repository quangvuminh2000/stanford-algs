"""
Problem: Calculate Inversions
Input: An array A of distinct integers
Output: The number of inversions of A - the number of pairs (i,j) of array indices with i < j and A[i] > A[j]
"""

from typing import List


def bf_inv(arr: List[int]) -> int:
    num_inv = 0
    n = len(arr)
    for i in range(n - 1):
        for j in range(i, n):
            if arr[i] > arr[j]:
                num_inv += 1

    return num_inv


def merge_inv(arr: List[int]) -> int:
    n = len(arr)

    return mergeSort(arr, n)


def mergeSort(arr: List[int], n: int):
    temp_arr = [0] * n
    return _mergeSort(arr, temp_arr, 0, n - 1)


def _mergeSort(arr, temp_arr, left, right):
    inv_count = 0

    if left < right:
        # mid: divide array into two sub-arrays
        mid = (left + right) // 2

        # Calculate inversions in the left sub-array
        inv_count += _mergeSort(arr, temp_arr, left, mid)

        # Calculate inversions in the right sub-array
        inv_count += _mergeSort(arr, temp_arr, mid + 1, right)

        # Calculate inversions in the split case
        inv_count += merge(arr, temp_arr, left, mid, right)
    return inv_count


def merge(arr, temp_arr, left, mid, right):
    i = left  # start left
    j = mid + 1  # start right
    k = left  # start of sorted
    inv_count = 0

    while i <= mid and j <= right:
        # No inversion
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:  # Have inversion
            temp_arr[k] = arr[j]
            k += 1
            j += 1
            inv_count += mid - i + 1

    # Copy the left sub into the sorted
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1

    # Copy the right sub into the sorted
    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1

    # Turn the original array into sorted
    for idx in range(left, right + 1):
        arr[idx] = temp_arr[idx]

    return inv_count


def count_inv(input_path: str):
    with open(input_path, "r") as f:
        data = [int(l) for l in f.readlines()]

    num_inv = merge_inv(data)

    return num_inv
