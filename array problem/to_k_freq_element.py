"""
Problem: 347. Top K Frequent Elements
Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
"""

### My solution with time complexity O(nlogn) and space complexity O(n)
def topKFrequent(nums, k):
        map = {x: nums.count(x) for x in nums}
        sortedd = sorted(map.values(), reverse= True)
        trimm = sortedd[:k]
        print(map)
        res = []
        for i in  trimm:
            j = [key for key,value in map.items() if value == i]
            map.pop(j[0])
            res.append(j[0])
            
        return res

print(topKFrequent([1,1,1,2,2,3], 2))

# Optimized solution with time complexity O(n) and space complexity O(n)

def topKFrequent(nums, k):
    map = {x: nums.count(x) for x in nums}
    bucket = [[] for _ in range(len(nums)+1)]
    for key, value in map.items():
        bucket[value].append(key)
    res = []
    for i in range(len(bucket)-1, -1, -1):
        if bucket[i]:
            res.extend(bucket[i])
        if len(res) == k:
            break
    return res

print(topKFrequent([1,1,1,2,2,3], 2))