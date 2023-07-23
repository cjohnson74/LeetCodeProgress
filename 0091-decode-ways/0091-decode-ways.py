class Solution:
    def numDecodings(self, s: str) -> int:
        one, two = 1, 1
        
        for i in range(len(s)-1, -1, -1):
            temp = 0
            if s[i] != '0':
                temp = one
                
            if (i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i + 1] in '0123456')):
                temp += two
                
            two = one
            one = temp
            
        return one
                