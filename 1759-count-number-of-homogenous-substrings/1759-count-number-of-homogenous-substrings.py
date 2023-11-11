class Solution:
    def countHomogenous(self, s: str) -> int:
        count = 0
        currStrk = 0
        MOD = 10 ** 9 + 7
        
        for i in range(len(s)):
            if i == 0 or (s[i] == s[i-1]):
                currStrk += 1
            else:
                currStrk = 1
            count = (count + currStrk) % MOD
        return count