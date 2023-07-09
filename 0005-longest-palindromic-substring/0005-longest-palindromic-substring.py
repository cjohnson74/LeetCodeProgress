class Solution:
    def longestPalindrome(self, s: str) -> str:
        # loop through array
        # have pointers starting at letter
        # pointers go out while they are in bounds and while the string is a pali
        # keep track of result
        # check len of currString in while loop and update result
        # time: O(n^2) n being the number of letters in the string
        # space: O(n) n being the length of our result/inputstring
        
        result = ''
        greatestLength = 0
        
        for i in range(len(s)):
            # check odds
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                currLength = right - left + 1
                if currLength > greatestLength:
                    result = s[left:right+1]
                    greatestLength = currLength
                left -= 1
                right += 1
                
            # check evens
            left, right = i, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                currLength = (right - left + 1)
                if currLength > greatestLength:
                    result = s[left:right+1]
                    greatestLength = currLength
                left -= 1
                right += 1
                
        return result