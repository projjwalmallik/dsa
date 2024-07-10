def selection_sort(arr):
    for i in range(len(arr)):
        min_m = arr[i]
        for j in range(i, len(arr)):
            if arr[j] < min_m:
                min_m = arr[j]
                arr[j] = arr[i]
        arr[i] = min_m
    return arr

print(selection_sort([34,3,645,32,54,34]))