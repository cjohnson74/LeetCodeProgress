class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combos = []
        
        def dfs(i, combo, currSum):
            if currSum == target:
                combos.append(combo.copy())
                return
            
            if (i >= len(candidates)) or (currSum > target):
                return
            
            combo.append(candidates[i])
            dfs(i, combo, currSum + candidates[i])
            
            combo.pop()
            dfs(i + 1, combo, currSum)
            
        dfs(0, [], 0)
        return combos