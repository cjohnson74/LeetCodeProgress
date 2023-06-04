class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftPnt = 0
        rightPnt = len(numbers)-1
        
        while leftPnt < rightPnt:
            currVal = numbers[leftPnt] + numbers[rightPnt]
            if currVal < target:
                leftPnt += 1
            elif currVal > target:
                rightPnt -= 1
            else:
                return [leftPnt+1, rightPnt+1]
        
