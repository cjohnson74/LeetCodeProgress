class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        LRow, RRow = 0, len(matrix)-1
        row = -1
        
        while LRow <= RRow:
            midRow = (LRow + RRow) / 2
            if matrix[midRow][0] < target:
                LRow = midRow + 1
                row = midRow
            elif matrix[midRow][0] > target:
                RRow = midRow - 1
            else:
                return True
            
        LCol, RCol = 0, len(matrix[0]) - 1
        midCol = -1
        
        while LCol <= RCol:
            midCol = (LCol + RCol) / 2
            if matrix[row][midCol] < target:
                LCol = midCol + 1
            elif matrix[row][midCol] > target:
                RCol = midCol - 1
            else:
                return True
        
        return False