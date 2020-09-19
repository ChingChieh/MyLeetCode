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