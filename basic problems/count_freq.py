def count_freq(arr):
    freq = {}
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    for i in freq:
        print(i, freq[i])
    return

count_freq([1,1,3,1,2,2,4,3])