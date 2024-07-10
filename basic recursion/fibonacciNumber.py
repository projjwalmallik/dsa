# Problem Statement: Given an integer N. Print the Fibonacci series  for every number up to the Nth term.

def fibonacciNumber(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacciNumber(n-1) + fibonacciNumber(n-2)

def print_fibonacci(n):
    if n <= 0:
        return
    for i in range(n):
        print(fibonacciNumber(i), end = " ")
    print()
    return
    

    
print(print_fibonacci(6))