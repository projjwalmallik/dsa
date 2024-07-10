def max_min_freq(arr):
    freq = {}
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    max_freq = max(freq.values())
    min_freq = min(freq.values())
    print(max_freq, min_freq)
    return

max_min_freq([1,2,1,2,3,6,6,2,3])