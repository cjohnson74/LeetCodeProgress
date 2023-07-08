class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left <= right:
            print(left, right)
            if not self.alphaNum(s[left]):
                left += 1
                continue
            if not self.alphaNum(s[right]):
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
            
        return True
            
    def alphaNum(self, lett):
        return ((ord('a') <= ord(lett) <= ord('z')) or
                (ord('A') <= ord(lett) <= ord('Z')) or
                (ord('0') <= ord(lett) <= ord('9')))
        
        
    