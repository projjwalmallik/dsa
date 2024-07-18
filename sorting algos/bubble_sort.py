def bubble_sort(arr):
    for i in range(len(arr)-1, 1, -1):
        for j in range(1,i-1):
            if arr[j] < arr[j-1]:
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
    return arr

print(bubble_sort([1,32,2,65,12,57]))

def bubble_sorting(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
