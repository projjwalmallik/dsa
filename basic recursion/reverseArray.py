def reverseArray(arr):
    if len(arr) == 0:
        return []
    print(arr[:-1])
    return [arr[-1]] + reverseArray(arr[:-1])


print(reverseArray([1, 2, 3, 4, 5])) # [5, 4, 3, 2, 1]