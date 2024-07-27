"""
String Encode and Decode
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]

"""
def encode(strs):
    return ''.join([str(len(s)) + '#' + s for s in strs])

def decode(s): 
    res = []
    i = 0
    while i < len(s):
        j = s.find('#', i)
        i = j + 1 + int(s[i:j])
        res.append(s[j+1:i])
    return res

print(encode(["leet","code","love","you"]))
print(decode("4#neet4#code4#love3#you"))
