class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # [1,1,2,3,3,4,4,8,8]
        #  L M   R
        # odd:X even:O
        # +1 ==:O  -1==:X  +1!=:X -1!=:O
        # move LP
        # odd:O even:X
        # +1 ==:X  -1==:O  +1!=:O -1!=:X
        # move LP
        # odd:O even:X
        # +1 ==:O  -1==:O  +1!=:X -1!=:X
        # return mid
        # odd:O even:X
        # +1 ==:O  -1==:X  +1!=:X -1!=:O
        # move RP
        # odd:X even:O
        # +1 ==:X  -1==:O  +1!=:O -1!=:X
        # move RP
        
        L, R = 0, len(nums) - 1
        
        while L < R:
            mid = (L + R) // 2

            # Ensure mid is even (if it's odd, decrement it by 1)
            if mid % 2 == 1:
                mid -= 1

            # Check pair alignment
            if nums[mid] == nums[mid + 1]:
                # If they are equal, the unique element is in the right half
                L = mid + 2
            else:
                # If they are not equal, the unique element is in the left half
                R = mid

        return nums[L]
                