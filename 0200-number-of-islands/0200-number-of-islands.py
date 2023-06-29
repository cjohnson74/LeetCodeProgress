class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        res = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        
        def bfs(row, col):
            queue = collections.deque()
            visited.add((row, col))
            queue.append((row, col))
            
            while queue:
                currRow, currCol = queue.popleft()
                
                deltas = [(0,1),(0,-1),(1,0),(-1,0)]
                for delta in deltas:
                    deltaRow, deltaCol = delta
                    rowNeighbor = currRow + deltaRow
                    colNeighbor = currCol + deltaCol
                    if rowNeighbor >= 0 and rowNeighbor < len(grid) and colNeighbor >= 0 and colNeighbor < len(grid[0]) and (rowNeighbor, colNeighbor) not in visited:
                        if grid[rowNeighbor][colNeighbor] == '1':
                            queue.append((rowNeighbor, colNeighbor))
                            visited.add((rowNeighbor, colNeighbor))
        
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1' and (row, col) not in visited:
                    bfs(row, col)
                    res += 1
                    
        return res