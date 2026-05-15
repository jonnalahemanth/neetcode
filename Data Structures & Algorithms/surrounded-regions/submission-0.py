class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return 

        rows, cols = len(board), len(board[0])

        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            if r<0 or c<0 or r>=rows or c>=cols:
                return
            
            if board[r][c] != 'O':
                return

            board[r][c] = 'T'
            
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                dfs(nr, nc)

        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols-1)

        for c in range(cols):
            dfs(0, c)
            dfs(rows-1, c)    

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'T':
                    board[row][col] = 'O'


        