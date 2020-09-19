class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = dict()
        i = 0
        result = 0
        for idx, val in enumerate(s):
            if val in hashMap:
                i = max(hashMap[val], i)
            hashMap[val] = idx + 1
            result = max(result, idx - i + 1)
        return result
    
'''
Sliding Window Optimized:
using the distance of i and idx to measrue the length of longest substring
advantage: If s[j] have a duplicate in the range [i,j) with index j', don't need to 
           remove the itesm before j'(this is what "i = max(hashMap[val, i])" does) 
'''