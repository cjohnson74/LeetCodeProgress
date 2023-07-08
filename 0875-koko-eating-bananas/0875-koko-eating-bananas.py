class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search
        # left, right = 0, max(piles)
        # loop through piles
        # keep total for each loop
        # if total is less than 8 then right = min - 1
        # if total is greater than 8 then right = min + 1
        # else return min
        
        
        left, right = 1, max(piles)
        minSpeed = max(piles)
        
        while left <= right:
            mid = (left + right) // 2
            
            currHours = 0
            for pile in piles:
                currHours += math.ceil(pile / mid)

            if currHours > h:
                left = mid + 1
            else:
                minSpeed = min(mid, minSpeed)
                right = mid - 1

        return minSpeed