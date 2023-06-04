class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowsVals = collections.defaultdict(set)
        colsVals = collections.defaultdict(set)
        squaresVals = collections.defaultdict(set) # key: (row // 3, col // 3)
        
        for row in range(9):
            for col in range(9):
                currVal = board[row][col]
                if currVal == '.':
                    continue
                elif (currVal in rowsVals[row] or
                      currVal in colsVals[col] or
                      currVal in squaresVals[(row // 3, col // 3)]):
                    return False
                rowsVals[row].add(currVal)
                colsVals[col].add(currVal)
                squaresVals[(row // 3, col // 3)].add(currVal)
                
        return True