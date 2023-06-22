class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        l = 0
        longestLen = 0
        highestFreq = 0
        highestFreqLett = ''
        
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            highestFreq = max(window[s[r]], highestFreq)
            
            while ((r - l + 1) - highestFreq) > k:
                window[s[l]] -= 1
                l += 1
                    
            longestLen = max(longestLen, r - l + 1)
        
        return longestLen