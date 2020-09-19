class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = set()
        result = 0
        i, j = 0, 0
        while(i < len(s) and j < len(s)):
            if s[j] in longest:
                result = max(result, len(longest))
                longest.remove(s[i])
                i = i + 1
            else:
                longest.add(s[j])
                j = j + 1
                
        result = max(result, len(longest))
        return result

'''
Sliding Window: using i, j as bounds of the longest substing and "longest" as a set() to record 
                current char in the range [i,j). This approach needs keep deleting char in the set
                once it found the duplicate and moving i one by one to find the right bound
'''