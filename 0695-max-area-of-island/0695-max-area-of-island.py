class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        
        def bfs(row, col):
            stack = collections.deque()
            stack.append((row, col))
            area = 0
            
            while stack:
                row, col = stack.pop()
                grid[row][col] = 0
                area += 1
                
                deltas = [(0,1),(0,-1),(1,0),(-1,0)]
                for deltaRow, deltaCol in deltas:
                    neighborRow, neighborCol = row + deltaRow, col + deltaCol
                    if neighborRow >= 0 and neighborRow < len(grid) and neighborCol >= 0 and neighborCol < len(grid[0]) and grid[neighborRow][neighborCol] == 1:
                        area += bfs(neighborRow, neighborCol)
                    
            return area
            
            
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    maxArea = max(bfs(row, col), maxArea)
                    
        return maxArea