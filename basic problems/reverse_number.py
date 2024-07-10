def reverse_number(n):
    return int(str(n)[::-1])

number = reverse_number(123)
print(number) # 321

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1: Input: x = 123 Output: 321

def reverse(self, x: int) -> int:
        if x >= 0:
            y = str(x)
            z = y[::-1]
            if -2**31 <= int(z) <=2**31:
                return int(z)
            else:
                return 0
        if x < 0:
            y = str(x*(-1))
            z = y[::-1]
            if -2**31 <= int(z)*(-1) <=2**31:
                return int(z)*(-1)
            else:
                return 0      
           

        


            
            


        