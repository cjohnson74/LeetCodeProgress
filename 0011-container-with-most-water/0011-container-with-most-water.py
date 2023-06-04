class Solution:
    def maxArea(self, height: List[int]) -> int:
        leftPoint = 0
        rightPoint = len(height)-1
        currMax = 0
        
        while leftPoint < rightPoint:
            currWater = min(height[leftPoint], height[rightPoint]) * (rightPoint - leftPoint)
            currMax = max(currWater, currMax)
            if height[leftPoint] <= height[rightPoint]:
                leftPoint += 1
            else:
                rightPoint -= 1
        
        return currMax