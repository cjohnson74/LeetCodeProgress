class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        nums.sort()
        
        def backtrack(currSet, idx):
            print(currSet, idx)
            if idx == len(nums):
                subsets.append(currSet[::])
                return
            
            # all subsets that include nums[i]
            currSet.append(nums[idx]);
            backtrack(currSet, idx + 1)
            currSet.pop()
            
            # all subsets that do not include nums[i]
            while idx + 1 < len(nums) and nums[idx] == nums[idx+1]:
                idx += 1
            backtrack(currSet, idx + 1)
            
            # dfs(currSet, idx)
            
        backtrack([], 0)
        return subsets