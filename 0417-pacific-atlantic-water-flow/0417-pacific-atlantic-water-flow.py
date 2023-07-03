class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        cells = []
        pacific = {}
        atlantic = {}
        
        def dfs(row, col, prevHeight, ocean):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or (row,col) in ocean:
                return
            
            if heights[row][col] < prevHeight:
                return
            
            ocean[(row,col)] = True
            
            deltas = [[0,1],[0,-1],[1,0],[-1,0]]
            for [rowDelta, colDelta] in deltas:
                rowNeighbor = row + rowDelta
                colNeighbor = col + colDelta
                if (rowNeighbor, colNeighbor) not in ocean:
                    dfs(rowNeighbor, colNeighbor, heights[row][col], ocean)
                
            
        for row in range(ROWS):
            if (row, 0) not in pacific:
                dfs(row, 0, heights[row][0], pacific)
            if (row,COLS-1) not in atlantic:
                dfs(row, COLS-1, heights[row][COLS-1], atlantic)
        for col in range(COLS):
            if (0,col) not in pacific:
                dfs(0, col, heights[0][col], pacific)
            if (ROWS-1,col) not in atlantic:
                dfs(ROWS-1, col, heights[ROWS-1][col], atlantic)
        # for row in range(ROWS):
        #     if (row,COLS-1) not in atlantic:
        #         atlantic[(row, COLS-1)] = True
        #         dfs(row, COLS-1, 0, atlantic)
        # for col in range(COLS):
        #     if (ROWS-1,col) not in atlantic:
        #         atlantic[(ROWS-1, col)] = True
        #         dfs(ROWS-1, col, 0, atlantic)
                
        for row in range(ROWS):
            for col in range(COLS):
                if ((row, col) in pacific) and ((row, col) in atlantic):
                    cells.append([row, col])
                    
        return cells