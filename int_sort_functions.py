import time
import heapq


def insertion_sort(arr):
    time1 = time.perf_counter()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    time2 = time.perf_counter()
    total_time = (time2 - time1)
    return total_time


def bubble_sort(arr):
    time1 = time.perf_counter()

    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    time2 = time.perf_counter()
    total_time = (time2 - time1)
    return total_time


def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):

        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    time1 = time.perf_counter()

    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

    time2 = time.perf_counter()
    total_time = (time2 - time1)
    return total_time


def selection_sort(list2):
    time1 = time.perf_counter()

    n = len(list2)
    for i in range(0, n):
        min_val = i
        for j in range(i + 1, n):
            if list2[j] < list2[min_val]:
                min_val = j
        list2[i], list2[min_val] = list2[min_val], list2[i]

    time2 = time.perf_counter()
    total_time = (time2 - time1)
    return total_time


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap

        heapify(arr, n, largest)


def heap_sort(arr):
    time1 = time.perf_counter()

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # swap
        heapify(arr, i, 0)

    time2 = time.perf_counter()
    total_time = (time2 - time1)
    return total_time


def heap_sort_2(arr):
    time1 = time.perf_counter()

    heapq.heapify(arr)
    result = []
    while arr:
        result.append(heapq.heappop(arr))

    time2 = time.perf_counter()
    total_time = (time2 - time1)
    return total_time


def shell_sort(arr, list_len):
    time1 = time.perf_counter()

    interval = list_len // 2
    while interval > 0:
        for i in range(interval, list_len):
            temp = arr[i]
            j = i
            while j >= interval and arr[j - interval] > temp:
                arr[j] = arr[j - interval]
                j -= interval
            arr[j] = temp
        interval //= 2

    time2 = time.perf_counter()
    total_time = (time2 - time1)
    return total_time


def counting_sort(array, place):
    time1 = time.perf_counter()

    size = len(array)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]

    time2 = time.perf_counter()
    total_time = (time2 - time1)
    return total_time


def radix_sort(array):
    time1 = time.perf_counter()

    max_element = max(array)
    place = 1
    while max_element // place > 0:
        counting_sort(array, place)
        place *= 10

    time2 = time.perf_counter()
    total_time = (time2 - time1)
    return total_time


def cocktail_sort(arr):
    time1 = time.perf_counter()

    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False

        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break
        swapped = False
        end = end - 1

        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        start = start + 1

    time2 = time.perf_counter()
    total_time = (time2 - time1)
    return total_time


def gnome_sort(arr):
    time1 = time.perf_counter()
    n = len(arr)
    i = 1

    while i < n:
        if i == 0 or arr[i] >= arr[i - 1]:
            i += 1
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1

    time2 = time.perf_counter()
    total_time = (time2 - time1)
    return total_time


def pigeonhole_sort(arr):
    time1 = time.perf_counter()

    min_val = min(arr)
    max_val = max(arr)

    pigeonholes = [[] for _ in range(max_val - min_val + 1)]

    for x in arr:
        pigeonholes[x - min_val].append(x)

    sorted_array = []
    for hole in pigeonholes:
        sorted_array.extend(hole)

    time2 = time.perf_counter()
    total_time = (time2 - time1)
    return total_time


def bead_sort(a, length):
    time1 = time.perf_counter()

    maximum = a[0]
    for i in range(1, length):
        if a[i] > maximum:
            maximum = a[i]

    beads = [[0 for _ in range(maximum)] for _ in range(length)]

    for i in range(length):
        for j in range(a[i]):
            beads[i][j] = 1

    for j in range(maximum):
        total = 0
        for i in range(length):
            total += beads[i][j]
            beads[i][j] = 0
        for i in range(length - 1, length - total - 1, -1):
            beads[i][j] = 1

    result = [0] * length
    for i in range(length):
        total2 = 0
        for j in range(maximum):
            total2 += beads[i][j]
        result[i] = total2

    time2 = time.perf_counter()
    total_time = (time2 - time1)
    return total_time
