def print_1toN(n):
    if n == 0:
        return
    print(n)
    print_1toN(n-1)

print_1toN(5) # 5 4 3 2 1