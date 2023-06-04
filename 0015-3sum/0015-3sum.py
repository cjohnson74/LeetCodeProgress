class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for idx, num in enumerate(nums):
            if idx > 0 and num == nums[idx - 1]:
                continue
                
            leftPoint = idx+1
            rightPoint = len(nums) - 1
            
            while leftPoint < rightPoint:
                threeSum = num + nums[leftPoint] + nums[rightPoint]
                if threeSum < 0:
                    leftPoint += 1
                elif threeSum > 0:
                    rightPoint -= 1
                else:
                    res.append([num, nums[leftPoint], nums[rightPoint]])
                    leftPoint += 1
                    while nums[leftPoint] == nums[leftPoint - 1] and leftPoint < rightPoint:
                        leftPoint += 1
        return res