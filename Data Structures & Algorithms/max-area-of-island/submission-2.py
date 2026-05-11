class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        

        def dfs(r, c):
            if r<0 or c<0 or r>=rows or c>=cols:
                return 0

            if grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            
            area = 1

            for dr, dc in dirs:
                nr, nc = r+dr, c+dc

                area += dfs(nr, nc)

            return area

        
        max_area = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    max_area = max(dfs(row, col), max_area)

        return max_area
        