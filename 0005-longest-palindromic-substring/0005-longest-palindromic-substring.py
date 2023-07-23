class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestSubstringLeft, longestSubstringRight = 0, 0
        longestSubstringLen = 0
        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                currLength = right - left + 1
                if longestSubstringLen < currLength:
                    longestSubstringLeft, longestSubstringRight = left, right + 1
                    longestSubstringLen = currLength
                left -= 1
                right += 1
            
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                currLength = right - left + 1
                if longestSubstringLen < currLength:
                    longestSubstringLeft, longestSubstringRight = left, right + 1
                    longestSubstringLen = currLength
                left -= 1
                right += 1
                    
        return s[longestSubstringLeft:longestSubstringRight]
            