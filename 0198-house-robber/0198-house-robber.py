class Solution:
    def rob(self, nums: List[int]) -> int:
        # dfs
        # base case reach end of array
        # if house == len(nums) return nums[house]
        # if house > len(nums) return 0
        # keep a currMaxRobbed
            # loop through each house except the one to the right
            # currMaxRobbed = max(currMaxRobbed, dfs(nextHouse)
        # return nums[cost] + curMaxRobbed
        # O(n!)
        # O(n!) depth of the decision tree
        # reduce time: O(n) keeping a memo
        # reduce space: O(n) keeping a memo of the length of the houses and reduces repeated work
        
        rob1, rob2 = 0, 0
        
        for house in nums:
            temp = max(house + rob1, rob2)
            rob1 = rob2
            rob2 = temp
            
        return rob2
        
#         def dfs(house, memo = {}):
#             if house in memo:
#                 return memo[house]
            
#             if house == len(nums)-1:
#                 return nums[house]
            
#             if house > len(nums)-1:
#                 return 0
            
#             currMaxRobbed = 0
#             for nextHouse in range(house + 2, len(nums)):
#                 currMaxRobbed = max(currMaxRobbed, dfs(nextHouse))
            
#             memo[house] = nums[house] + currMaxRobbed
#             return memo[house]
        
#         return max(dfs(0), dfs(1))