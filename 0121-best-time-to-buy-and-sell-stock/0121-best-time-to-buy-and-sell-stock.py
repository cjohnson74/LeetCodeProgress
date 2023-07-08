class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left and right pointer
        # keep track of max profit seen
        # increment right pointer until prices[right] < prices[left]
            # then make left pointer = right pointer
        # while right pointer < len(prices)
        # return maxProfit
        
        maxProfit = 0
        left, right = 0, 1
        
        while right < len(prices):
            profit = prices[right] - prices[left]
            maxProfit = max(maxProfit, profit)
            
            if prices[right] < prices[left]:
                left = right
            else:
                right += 1
                
        return maxProfit