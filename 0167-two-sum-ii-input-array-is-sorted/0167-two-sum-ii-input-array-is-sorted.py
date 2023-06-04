class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pnt1 = 0
        pnt2 = len(numbers)-1
        
        while numbers[pnt1] + numbers[pnt2] != target:
            currVal = numbers[pnt1] + numbers[pnt2]
            if currVal < target:
                pnt1 += 1
            else:
                pnt2 -= 1
        
        return [pnt1+1, pnt2+1]