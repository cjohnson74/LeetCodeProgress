class Solution:
    def countSubstrings(self, s: str) -> int:
        # loop through s
        # check for palidromes by have a left and right pointer starting at middle and expanding
        # check odd by starting at left, right = i, i
        # check even by starting at left, right = i, i+1
        # in while loops increase the number of palidromes by 1
        
        numOfPalindromes = 0
        
        for i in range(len(s)):
            # check odd pali
            numOfPalindromes += self.numPali(s, i, i)
                
            # check even pali
            numOfPalindromes += self.numPali(s, i, i+1)
                
        return numOfPalindromes
    
    def numPali(self, s, left, right):
        result = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            result += 1
            left -= 1
            right += 1
            
        return result