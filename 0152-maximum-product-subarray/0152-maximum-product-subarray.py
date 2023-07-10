class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp
        # maintain max and min of substring
        # if zero set max and min to 1
        # return max
        
        res = max(nums)
        currMax, currMin = 1, 1
        
        for num in nums:
            if num == 0:
                currMax = 1
                currMin = 1
            else:
                temp = max((num * currMin), (num * currMax), num)
                currMin = min((num * currMin), (num * currMax), num)
                currMax = temp
                res = max(res, currMax)
            
        return res