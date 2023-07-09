class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        
        for step in range(len(dp)-1, -1, -1):
            if step == n or step + 1 == n:
                dp[step] = 1
            else:
                dp[step] = dp[step + 1] + dp[step + 2]
                
        return dp[0]