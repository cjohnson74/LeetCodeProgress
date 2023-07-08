class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search on the lists
        # binary search on the list with our number
        # left, right = 0, len(matrix) - 1
        # leftNum, rightNum = matrix[left][0], matrix[right][-1]
        # mid = (left + right) // 2
        # minNum = matrix[mid][0]
        # while left <= right
        
        # after loop we will have the index of the array that the target is in
        # binary search the array for target
        # leftNum, rightNum = array[left], array[right]
        # if array[mid] == target: return True
        
        # return False
        
        top, bot = 0, len(matrix) - 1
        
        while top <= bot:
            row = (top + bot) // 2
            
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        
        if not (top <= bot):
            return False
        
        left, right = 0, len(matrix[0]) - 1
        row = (top + bot) // 2
        
        while left <= right:
            mid = (left + right) // 2
            midNum = matrix[row][mid]
            
            if target > midNum:
                left = mid + 1
            elif target < midNum:
                right = mid - 1
            else:
                return True
            
        return False