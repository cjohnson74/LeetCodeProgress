class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        L, R = 0, len(nums) - 1
        res = []
        # [-5,-3,-2,-1]
        #  L  M      R
        #  
        
        while L <= R:
            Lnum, Rnum = nums[L] * nums[L], nums[R] * nums[R]
            if Lnum > Rnum:
                res.append(Lnum)
                L += 1
            else:
                res.append(Rnum)
                R -= 1
                
        return reversed(res)
