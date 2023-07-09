class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1] * 3
        
        for step in range(n-2, -1, -1):
            dp[0] = dp[1] + dp[2]
            dp[2] = dp[1]
            dp[1] = dp[0] 
                
        return dp[0]