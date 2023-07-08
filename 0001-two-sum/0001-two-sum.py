class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answers = {}
        for i in range(len(nums)):
            if nums[i] not in answers:
                answers[target-nums[i]] = i
        
        for i in range(len(nums)):
            if nums[i] in answers and i != answers[nums[i]]:
                return [i, answers[nums[i]]]
                
                