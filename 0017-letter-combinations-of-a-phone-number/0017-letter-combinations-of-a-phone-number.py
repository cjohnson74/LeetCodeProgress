class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if len(digits) == 0:
            return res
        
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
            if i >= len(digits):
                res.append(currCombo)
                return
            
            for lett in digitToLettMap[digits[i]]:
                currCombo += lett
                backtrack(i + 1, currCombo)
                currCombo = currCombo[:-1]
                
        backtrack(0, '')
        return res