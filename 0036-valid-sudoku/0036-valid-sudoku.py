class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create graph of all nine boxes
        # keys: 1-9, values: [values in the box not including periods]
        # if value is less than 1 or greater than 9 return false
        maxRow = 3;
        maxCol = 3;
        startRow = 0;
        startCol = 0;
        currBox = 1;
        while currBox < 10:
            boxValues = []
            for row in range(startRow, maxRow):
                for col in range(startCol, maxCol):
                    print(row, col)
                    currVal = board[row][col]
                    if currVal != '.':
                        if currVal in boxValues:    # check if currVal already exists in the box
                            return False    # if dupe then return false
                        else:
                            boxValues.append(currVal)
            print(boxValues)
            currBox += 1
            print(currBox)
            startRow = maxRow
            maxRow = startRow + 3
            if maxRow > 9:
                startCol = maxCol
                maxCol = startCol + 3
                startRow = 0
                maxRow = 3
                
        # check every row for dupe
        for row in range(0, 9):
            rowVals = {}
            for col in range(0, 9):
                currVal = board[row][col]
                if currVal != '.':
                    if currVal in rowVals:
                        return False
                    else:
                        rowVals[currVal] = ''
                
    
        # check every col for dupes
        for col in range(0, 9):
            colVals = {}
            for row in range(0, 9):
                currVal = board[row][col]
                if currVal != '.':
                    if currVal in colVals:
                        return False
                    else:
                        colVals[currVal] = ''
        
        return True