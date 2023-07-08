class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search
        # left and right
        # while left <= right
        # mid = (left + right) // 2
        # if nums[mid] == target: return mid
        # if target < nums[mid]: right = mid - 1
        # if target > nums[mid]: left = mid + 1
        # return -1 if reach the end
        
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target: return mid
            
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
                
        return -1