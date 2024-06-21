class Solution:
    def feasible(self, weights, capPerDay, days):
        currWeight = 0
        
        for weight in weights:
            if currWeight + weight > capPerDay:
                currWeight = weight
                days -= 1
                if days == 0:
                    return False
            else:
                currWeight += weight
        return True
            
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        L, R = max(weights), sum(weights)
        maxCap = 0
        
        while L <= R:
            mid = (L + R) // 2
            if self.feasible(weights, mid, days):
                maxCap = mid
                R = mid - 1
            else:
                L = mid + 1
                
        return maxCap