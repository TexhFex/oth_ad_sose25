import random
import time


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def measure_sort(sort_function, n, time_limit=60):
    total_numbers = 0
    start_time = time.time()
    while time.time() - start_time < time_limit:
        numbers = [random.randint(0, 10000) for _ in range(n)]
        sorted_numbers = sort_function(numbers.copy())
        total_numbers += n
    return total_numbers


if __name__ == '__main__':
    n = 100000
    print("Starte Messung (60 Sekunden)...")

    start = time.time()
    bubble_total = measure_sort(bubble_sort, n)
    print("BubbleSort:\t{}".format(bubble_total))

    start = time.time()
    quick_total = measure_sort(quick_sort, n)
    print("QuickSort:\t{}".format(quick_total))

    start = time.time()
    merge_total = measure_sort(merge_sort, n)
    print("MergeSort:\t{}".format(merge_total))
