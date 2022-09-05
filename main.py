# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from binary_search import binary_search as bs
from selection_sort import selection_sort as sel_sort
from divide_n_conquer import recursive_len as r_len
from divide_n_conquer import recursive_largest as r_max
from quick_sort import quick_sort as q_s


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_list = [1, 2, 2, 4, 5, 6, 7, 8, 8, 9]

    # Binary Search dem
    print(bs(my_list, 5))
    print(bs(my_list, 3))

    # Selection Sort dem
    print(my_list[::-1])
    print(sel_sort(my_list[::-1]))

    # D-n-C dem
    print(r_len(my_list))
    print(r_len([0]))

    print(r_max([1]))
    print(r_max(my_list))

    # Quick sort dem
    print(q_s([1, 1, 1, 1, 1, 2, 1]))
    print(q_s([1]))
    print(q_s([]))
    print(q_s([5, 4, 3, 2, 1]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
