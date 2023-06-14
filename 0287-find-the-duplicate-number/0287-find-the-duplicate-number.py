class Solution:
    def findDuplicate(self, nums: List[int]) -> int:  
        slow, fast = 0, 0
        
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                break
                
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow