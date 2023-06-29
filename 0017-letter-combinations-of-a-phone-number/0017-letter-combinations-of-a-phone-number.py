class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToLettMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz" }
        
        def backtrack(i, currCombo):
            if len(currCombo) >= len(digits):
                res.append(currCombo)
                return
            
            for lett in digitToLettMap[digits[i]]:
                backtrack(i + 1, currCombo + lett)
                
        if digits:
            backtrack(0, '')
            
        return res