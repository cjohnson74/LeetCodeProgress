class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0
        
        def bfs(row, col):
            stack = collections.deque()
            stack.append((row, col))
            area = 1
            
            while stack:
                row, col = stack.pop()
                grid[row][col] = 0
                
                deltas = [(0,1),(0,-1),(1,0),(-1,0)]
                for deltaRow, deltaCol in deltas:
                    neighborRow, neighborCol = row + deltaRow, col + deltaCol
                    if neighborRow >= 0 and neighborRow < ROWS and neighborCol >= 0 and neighborCol < COLS and grid[neighborRow][neighborCol] == 1:
                        stack.append((neighborRow, neighborCol))
                        grid[neighborRow][neighborCol] = 0
                        area += 1
                    
            return area
            
            
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    maxArea = max(bfs(row, col), maxArea)
                    
        return maxArea