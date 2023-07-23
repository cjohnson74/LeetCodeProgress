class Solution:
    def countSubstrings(self, s: str) -> int:
        numOfSubstrings = 0
        
        for i in range(len(s)):
            numOfSubstrings += self.countPali(i, i, s)
            numOfSubstrings += self.countPali(i, i + 1, s)
                
        return numOfSubstrings
    
    def countPali(self, left, right, s):
        res = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            res += 1
            left -= 1
            right += 1
        return res