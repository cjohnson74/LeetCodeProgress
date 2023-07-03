class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(row, col):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or board[row][col] == 'X' or board[row][col] == 'NF':
                return
            
            board[row][col] = 'NF'
            
            deltas = [(0,1),(0,-1),(1,0),(-1,0)]
            for rowDelta, colDelta in deltas:
                rowNeighbor = row + rowDelta
                colNeighbor = col + colDelta
                dfs(rowNeighbor, colNeighbor)
            
            
        for row in range(ROWS):
            dfs(row, 0)
            dfs(row, COLS-1)
        for col in range(COLS):
            dfs(0, col)
            dfs(ROWS-1, col)
            
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                    
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'NF':
                    board[row][col] = 'O'