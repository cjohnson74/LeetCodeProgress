class Solution:
    def mySqrt(self, x: int) -> int:
        L, R = 0, x
        sqrt = 0
        
        while L <= R:
            mid = (L + R) // 2
            if mid * mid < x:
                sqrt = mid
                L = mid + 1
            elif mid * mid > x:
                R = mid - 1
            else:
                return mid
            
        return sqrt