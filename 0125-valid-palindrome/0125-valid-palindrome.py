class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        
        for lett in s:
            if lett.isalnum():
                newStr += lett.lower()
        if newStr == newStr[::-1]:
            return True
            
        return False