class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        L, R = 0, num
        
        while L <= R:
            mid = (L + R) // 2
            sqr = mid * mid
            if sqr == num:
                return True
            elif sqr > num:
                R = mid - 1
            else:
                L = mid + 1
                
        return False