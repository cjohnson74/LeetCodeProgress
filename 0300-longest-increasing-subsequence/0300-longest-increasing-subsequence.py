class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp
        # decision tree
        # for i in range(len(nums)):
        # dfs(i)
        # currMaxLen = 1
        # for j in range(len(nums)):
            # if nums[i] < nums[j]:
                # currMaxLen = max(currMaxLen, dfs(j) + 1)
        
        # return currMaxLen
        # time: n^2
        # space: n
        # time: n with memoization
        # space: n length of nums
        
        def dfs(i, memo = {}):
            if i in memo:
                return memo[i]
            if i == len(nums):
                return 0
            
            currMaxLen = 1
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    currMaxLen = max(currMaxLen, dfs(j) + 1)
            
            memo[i] = currMaxLen
            return currMaxLen
        
        maxLength = 0
        for i in range(len(nums)):
            maxLength = max(maxLength, dfs(i))
        
        return maxLength