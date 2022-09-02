def find_smallest(arr):
    smallest_index = 0
    smallest = arr[smallest_index]
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index


def selection_sort(arr):
    sorted_arr = []
    for i in range(len(arr)):
        smallest_ind = find_smallest(arr)
        sorted_arr.append(arr.pop(smallest_ind))
    return sorted_arr
