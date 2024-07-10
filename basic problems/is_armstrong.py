# Check if a number is Armstrong Number or not


# Problem Statement: Given an integer N, return true it is an Armstrong number otherwise return false.

# An Amrstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
def is_armstrongNumber(n):
    if n == 1 or n == 0:
        return True
    num = str(n)
    cnt = len(num)
    res = 0
    for i in num:
        res += int(i)**cnt
    return res == n

print(is_armstrongNumber(371))