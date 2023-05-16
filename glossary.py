def gloss_text(gloss_id):
    text = ""

    match gloss_id:
        case "Insertion Sort":
            text = "This algorithm works by iterating through an array and comparing each element with the elements that come before it, and then inserting the element into the correct position. This builds the final sorted array one element at a time.  "

        case "Bubble Sort":
            text = "Bubble sort is a simple sorting algorithm that steps through a list, compares adjacent elements, and swaps them if they are in the wrong order. This is repeated until the list is sorted. The largest element will be 'bubbled' up to the end of the list. "

        case "Quick Sort":
            text = "Quick sort uses a divide-and-conquer strategy to sort an array. It selects a 'pivot' element for the array and partitions the elements into two sub arrays, according to whether they are less than or greater than the pivot. The sub arrays are recursively sorted"

        case "Selection Sort":
            text = "This is a simple sort that repeatedly finds the minimum element of the array and moving it to the beginning or end of the sorted part of the array."

        case "Heap Sort":
            text = "Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure to sort an array or a list of elements. It works by building a binary heap from the array, which is a complete binary tree where the value of each node is greater than or equal to (or less than or equal to) the values of its children nodes. The root node of the heap is the maximum (or minimum) element of the array, and it is removed and added to the sorted portion of the array. The remaining elements are then re-arranged to maintain the heap property, and the process is repeated until the entire array is sorted."

        case "Heap Sort 2":
            text = "This is a heap sort using the built in Python library 'heapq'."

        case "Shell Sort":
            text = "Shell sort is a variation of insertion sort that is designed to improve the efficiency of the sorting algorithm by sorting elements that are far apart before sorting elements that are nearby. The algorithm works by performing multiple passes over the input array, each time sorting a subset of elements that are a fixed distance apart. The distance between elements that are compared and swapped decreases with each pass until it reaches 1, at which point the algorithm behaves like an ordinary insertion sort."

        case "Radix Sort":
            text = 'Radix sort is a non-comparative integer sorting algorithm that sorts data by processing individual digits or groups of digits that represent the same significant position in each element of the input array. The algorithm works by sorting the elements in the input array according to the values of their least significant digit, then sorting the elements again according to the values of their next least significant digit, and so on, until all digits have been processed and the array is sorted.'

        case "Cocktail Sort":
            text = "Cocktail sort, also known as bidirectional bubble sort, is a variation of the bubble sort algorithm that improves its performance by sorting the input array in both directions, alternately sorting from the beginning to the end and from the end to the beginning. The algorithm works by repeatedly iterating over the input array, comparing adjacent elements and swapping them if they are in the wrong order, until no more swaps are needed."

        case "Gnome Sort":
            text = "Gnome sort is a sorting algorithm that is similar to insertion sort in that it works by iteratively inserting each element in its correct position in a partially sorted array. However, unlike insertion sort, which always starts at the beginning of the array and works its way forward, gnome sort compares adjacent elements and swaps them if they are in the wrong order, effectively 'pushing' the larger elements toward the end of the array and the smaller elements toward the beginning."

        case "Pigeonhole Sort":
            text = "Pigeonhole sort is a sorting algorithm that works by distributing the elements of an input sequence into a set of pigeonholes, then extracting the elements in order from the pigeonholes. It is particularly useful when the range of input values is relatively small compared to the size of the input sequence."

        case "Bead Sort":
            text = "Bead sort, also known as gravity sort or batcher's sort, is a non-comparison-based sorting algorithm that works by simulating gravity on a set of beads arranged on a set of vertical rods. The algorithm is particularly efficient for sorting small integer arrays."

    return text
