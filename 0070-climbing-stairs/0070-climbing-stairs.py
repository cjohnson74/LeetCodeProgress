class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        
        def dfs(step, memo = {}):
            if step in memo:
                return memo[step]
            
            if step == n:
                return 1
            
            if step > n:
                return 0
            
            count = dfs(step + 1) + dfs(step + 2)
            memo[step] = count
            return dfs(step + 1) + dfs(step + 2)
            
        count += dfs(1) 
        count += dfs(2)
        return count