class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                return True
        return False