class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for a in range(1, amount + 1):
            for coin in coins:
                if (a - coin) >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - coin])
            
        return dp[amount] if dp[amount] != float('inf') else -1
        
#         def dfs(currAmount = amount, count = 0, memo = {}):
#             pos = str(currAmount) + ',' + str(count)
#             if pos in memo:
#                 return memo[pos]
            
#             if currAmount == 0:
#                 return count
            
#             if currAmount < 0:
#                 return float('inf')
            
#             currMin = float('inf')
#             for nextCoin in coins:
#                 currMin = min(currMin, dfs(currAmount - nextCoin, count + 1, memo))
                
#             memo[pos] = currMin
#             return currMin
        
# #         minCoins = float('inf')
        
# #         for coin in coins:
# #             minCoins = min(minCoins, dfs(coin, amount - coin, 1))
#         minCoins = dfs()
#         return minCoins if minCoins != float('inf') else -1
            