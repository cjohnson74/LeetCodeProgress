class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        
        def bfs(row, col):
            queue = [[row, col]]
            
            while queue:
                [currRow, currCol] = queue.pop(0)
                
                deltas = [[0,1],[0,-1],[1,0],[-1,0]]
                for delta in deltas:
                    [deltaRow, deltaCol] = delta
                    rowNeighbor = currRow + deltaRow
                    colNeighbor = currCol + deltaCol
                    if rowNeighbor >= 0 and rowNeighbor < len(grid) and colNeighbor >= 0 and colNeighbor < len(grid[0]):
                        if grid[rowNeighbor][colNeighbor] == '1':
                            queue.append([rowNeighbor, colNeighbor])
                            grid[rowNeighbor][colNeighbor] = '0'
        
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    grid[row][col] = '0'
                    bfs(row, col)
                    res += 1
                    
        return res