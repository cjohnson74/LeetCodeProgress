class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # [1,3,5,6] target = 2
        # LMR    
        L, R = 0, len(nums)-1

        while L <= R:
            mid = (L + R) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                R = mid - 1
            else:
                L = mid + 1
            
        return L