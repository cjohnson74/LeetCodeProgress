class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        minutes, fresh = 0, 0
        queue = deque()
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    queue.append([row, col])
            
        while queue and fresh > 0:
            for i in range(len(queue)):
                currRow, currCol = queue.popleft()
                deltas = [[0,1],[0,-1],[1,0],[-1,0]]
                for rowDelta, colDelta in deltas:
                    neighborRow, neighborCol = currRow + rowDelta, currCol + colDelta
                    if (neighborRow < 0 or neighborRow == ROWS or neighborCol < 0 or neighborCol == COLS or grid[neighborRow][neighborCol] != 1):
                        continue
                    queue.append([neighborRow, neighborCol])
                    grid[neighborRow][neighborCol] = 2
                    fresh -= 1
            minutes += 1
                    
        return minutes if fresh == 0 else -1