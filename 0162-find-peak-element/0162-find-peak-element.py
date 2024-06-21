class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # [1,4,1,3,5,6]
        #  L   M     R
        # [1,2,1,3,5,6]
        #          R LM
        
        L, R = 0, len(nums) - 1
        
        while L <= R:
            mid = (R + L) // 2
            LVal = nums[mid - 1] if mid != 0 else float("-inf")
            RVal = nums[mid + 1] if mid != len(nums) - 1 else float("-inf")
            # Right less then mid and left less then mid
            if nums[mid] > LVal and nums[mid] > RVal:
                return mid
            elif LVal >= RVal:
                R = mid - 1
            else:
                L = mid + 1
                