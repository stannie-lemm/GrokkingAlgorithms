# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from binary_search import binary_search as bs
from selection_sort import selection_sort as sel_sort

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

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
