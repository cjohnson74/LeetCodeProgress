class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        islands = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        
        def bfs(row, col):
            queue = collections.deque()
            visited.add((row, col))
            queue.append((row, col))
            
            while queue:
                currRow, currCol = queue.popleft()
                
                deltas = [(0,1),(0,-1),(1,0),(-1,0)]
                for deltaRow, deltaCol in deltas:
                    rowNeighbor, colNeighbor = currRow + deltaRow, currCol + deltaCol
                    if (rowNeighbor in range(rows) and 
                        colNeighbor in range(cols) and
                        grid[rowNeighbor][colNeighbor] == '1' and
                       (rowNeighbor, colNeighbor) not in visited):
                        queue.append((rowNeighbor, colNeighbor))
                        visited.add((rowNeighbor, colNeighbor))
        
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1' and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1
                    
        return islands