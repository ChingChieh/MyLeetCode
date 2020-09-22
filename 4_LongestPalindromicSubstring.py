class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        result = ""
        maxLen = 0
        for i in range(len(s) - 1):
            tmp = self.checkPalindromic(i, i, s)
            if len(tmp) > len(result):
                result = tmp

            tmp = self.checkPalindromic(i, i + 1, s)
            if len(tmp) > len(result):
                result = tmp

        return result

    def checkPalindromic(self, center1, center2, s):
        strLen = len(s)
        result = ""
        while center1 >= 0 and center2 < strLen:
            if s[center1] == s[center2]:
                result = s[center1:center2+1]
                center1 -= 1
                center2 += 1
            else:
                break

        return result
