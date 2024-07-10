def sumOfNFirstNaturalNumbers(n):
    if n == 0:
        return 0
    return n + sumOfNFirstNaturalNumbers(n - 1)

print(sumOfNFirstNaturalNumbers(5)) # 15