class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        cells = []
        pacific, atlantic = set(), set()
        
        def dfs(row, col, prevHeight, ocean):
            if (row,col) in ocean or row < 0 or row >= ROWS or col < 0 or col >= COLS or heights[row][col] < prevHeight:
                return
            
            ocean.add((row, col))
            
            deltas = [[0,1],[0,-1],[1,0],[-1,0]]
            for [rowDelta, colDelta] in deltas:
                rowNeighbor = row + rowDelta
                colNeighbor = col + colDelta
                if (rowNeighbor, colNeighbor) not in ocean:
                    dfs(rowNeighbor, colNeighbor, heights[row][col], ocean)
                
            
        for row in range(ROWS):
            dfs(row, 0, heights[row][0], pacific)
            dfs(row, COLS-1, heights[row][COLS-1], atlantic)
        for col in range(COLS):
            dfs(0, col, heights[0][col], pacific)
            dfs(ROWS-1, col, heights[ROWS-1][col], atlantic)
                
        for row in range(ROWS):
            for col in range(COLS):
                if ((row, col) in pacific) and ((row, col) in atlantic):
                    cells.append([row, col])
                    
        return cells