class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combos = []
        candidates.sort()
        
        def backtrack(currCombo, pos, currSum):
            if currSum == target:
                combos.append(currCombo.copy())
            if currSum > target:
                return
            
            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                currCombo.append(candidates[i])
                backtrack(currCombo, i + 1, currSum + candidates[i])
                currCombo.pop()
                
                prev = candidates[i]
        backtrack([], 0, 0)
        return combos