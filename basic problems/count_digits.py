# Count Digits
# Difficulty: EasyAccuracy: 30.45%Submissions: 210K+Points: 2

# Given a number n. Count the number of digits in n which evenly divide n. Return an integer, total number of digits of n which divides n evenly.

# Note :- Evenly divides means whether n is divisible by a digit i.e. leaves a remainder 0 when divided.

# Input: n = 12
# Output: 2
# Explanation: 1, 2 when both divide 12 leaves remainder 0.
# Input: n = 23
# Output 0
# Explanation: 2 and 3, none of them divide 23 evenly.

def count_digits(n):
    count = 0
    for i in str(n):
        if int(i) == 0:
            continue
        if n % int(i) == 0:
            count += 1
    print(count)

count_digits(363)