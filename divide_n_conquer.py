# Ex 1: sum and recursive sum

def my_sum(arr):
    res = 0
    for i in arr:
        res += i
    return res


def recursive_sum(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    return arr[0] + sum(arr[1:])


# Ex 2: recursive len

def recursive_len(arr):
    if len(arr) == 0:
        return 0
    return 1 + len(arr[1:])


# Ex 3: find the largest number in list

def recursive_largest(arr):
    if len(arr) == 1:
        return arr[0]
    return max(arr[0], recursive_largest(arr[1:]))

