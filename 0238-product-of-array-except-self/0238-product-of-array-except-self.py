class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0 for i in range(len(nums))]
        currProd = 1
        for i in range(0,len(nums)):
            temp = nums[i]
            output[i] = currProd
            currProd *= temp
            
        currProd = 1
        for i in range(len(nums)-1, -1, -1):
            temp = nums[i]
            output[i] *= currProd
            currProd *= temp
            
        return output