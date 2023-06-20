"""
Sorting - Implement two types of sorting algorithms: Merge sort and bubble sort.

https://github.com/karan/Projects
"""

import random

def merge_sort(numbers: list[int]) -> list[int]:
    if len(numbers) > 1:
        middle = len(numbers) // 2
        left = numbers[:middle]
        right = numbers[middle:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                numbers[k] = left[i]
                i += 1
            else:
                numbers[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            numbers[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            numbers[k] = right[j]
            j += 1
            k += 1


def bubble_sort(numbers: list[int]) -> list[int]:
    n = len(numbers)
    swapped = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                swapped = True
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        if not swapped:
            return


integers = [ random.randint(0, 100) for _ in range(100) ]
integers2 = integers.copy()
merge_sort(integers)
print(integers)
bubble_sort(integers2)
print(integers2)
assert integers == integers2