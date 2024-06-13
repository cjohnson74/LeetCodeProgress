class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # win = set()
        # win len <= k
        # if nums[i] == nums[j] return True
        
        # [1,0,1,1] k = 1
        #  LR
        # winSize = R - L
        # win = {}
        window = set()
        L = 0
        
        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
         
        return False
                