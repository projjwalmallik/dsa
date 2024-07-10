def print_n_times(n):
    if n == 0:
        return
    print("Hello")
    n -= 1
    print_n_times(n)

print_n_times(6)