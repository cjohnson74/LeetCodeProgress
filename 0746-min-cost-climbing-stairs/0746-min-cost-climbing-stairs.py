class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dfs
        # base case step == n: return cost[step]
        # base case step > n: return float('infinity')
        # at each step return min(dfs(step+1), dfs(step+2))
        
        # return min(dfs(step+1), dfs(step+2))
        # time: 2^n because we are making two decisions at every step and repeated work
        # space: n being the deepest branch in the decision tree
        # reduce time: O(n) using dp/memoization
        # space: n being the number of steps because we cut out repeated work with memo
        # time: O(n)
        # reduce space: O(1)
        
        cost.append(0)
        
        for step in range(len(cost)-3, -1, -1):
            cost[step] = cost[step] + min(cost[step + 1], cost[step + 2])
            
        return min(cost[0], cost[1])
        
#         def dfs(step, memo = {}):
#             if step in memo:
#                 return memo[step]
            
#             if step == len(cost)-1:
#                 return cost[step]
            
#             if step > len(cost) - 1:
#                 return 0
            
#             minCost = cost[step] + min(dfs(step + 1), dfs(step + 2))
#             memo[step] = minCost
#             return minCost
        
#         return min(dfs(0), dfs(1))