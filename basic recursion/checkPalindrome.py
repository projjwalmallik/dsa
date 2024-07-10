def checkPalindrome(s):
    if len(s) == 0 or len(s) == 1:
        return True
    if s[0] == s[-1]:
        print(s[1:-1])
        return checkPalindrome(s[1:-1])
    return False

print(checkPalindrome("racecar")) # True