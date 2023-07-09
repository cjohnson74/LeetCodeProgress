class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def robHelper(startHouse, endHouse):
            rob1, rob2 = 0, 0
            
            for house in range(startHouse, endHouse):
                newRob = max(nums[house] + rob1, rob2)
                rob1 = rob2
                rob2 = newRob
            
            return rob2
        
        # nums[0] is an edge case that is if len(nums) == 1 then that would be the max returned
        return max(nums[0], robHelper(0, len(nums)-1), robHelper(1, len(nums)))