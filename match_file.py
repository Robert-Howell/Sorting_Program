import random
from int_sort_functions import *


def sort_choice(arr_size, sort_type):
    array = [i for i in range(1, arr_size)]
    random.shuffle(array)
    total_time = 0

    match sort_type:
        case "Insertion Sort":
            total_time = insertion_sort(array)

        case "Bubble Sort":
            total_time = bubble_sort(array)

        case "Quick Sort":
            total_time = quick_sort(array, 0, len(array) - 1)

        case "Selection Sort":
            total_time = selection_sort(array)

        case "Heap Sort":
            total_time = heap_sort(array)

        case "Heap Sort 2":
            total_time = heap_sort_2(array)

        case "Shell Sort":
            total_time = shell_sort(array, arr_size-1)

        case "Radix Sort":
            total_time = radix_sort(array)

        case "Cocktail Sort":
            total_time = cocktail_sort(array)

        case "Gnome Sort":
            total_time = gnome_sort(array)

        case "Pigeonhole Sort":
            total_time = pigeonhole_sort(array)

        case "Bead Sort":
            total_time = bead_sort(array, arr_size - 1)

    return total_time
