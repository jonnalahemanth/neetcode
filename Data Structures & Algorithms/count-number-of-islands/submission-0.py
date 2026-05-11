class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])

        dcs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
        def dfs(r, c):
            if r<0 or c<0 or r>=rows or c>=cols:
                return
            
            if grid[r][c] == "0":
                return

            grid[r][c] = "0"
            for dr, dc in dcs:
                nr, nc = dr+r, dc+c
                dfs(nr, nc)



        islands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands += 1
                    dfs(row, col)

        return islands