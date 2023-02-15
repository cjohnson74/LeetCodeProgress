class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0 for i in range(len(nums))]
        currProd = 1
        for i in range(0,len(nums)):
            output[i] = currProd
            currProd *= nums[i]
            
        currProd = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= currProd
            currProd *= nums[i]
            
        return output