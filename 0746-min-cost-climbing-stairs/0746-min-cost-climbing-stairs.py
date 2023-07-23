class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one, two = cost[len(cost)-2], cost[len(cost)-1]
        
        for step in range(len(cost)-3, -1, -1):
            temp = one
            one = min(cost[step] + one, cost[step] + two)
            two = temp
            
        return min(one, two)