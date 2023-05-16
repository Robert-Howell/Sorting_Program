import random
import time

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def single_string_sort(size):
    char_list = []

    for i in range(size):
        char_list.append(random.choice(letters))

    time1 = time.perf_counter()
    char_list.sort()
    time2 = time.perf_counter()
    total_time = (time2 - time1)

    return total_time


def multi_string_sort(arr_length, str_size):
    char_list = []

    for i in range(arr_length):
        new_str = ""
        length = random.choice(range(str_size))
        for j in range(length):
            new_str += random.choice(letters)

        char_list.append(new_str)

    time1 = time.perf_counter()
    char_list.sort()
    time2 = time.perf_counter()
    total_time = (time2 - time1)

    return total_time
