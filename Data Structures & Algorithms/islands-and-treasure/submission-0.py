from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])

        q = deque()
        visit = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))

        dirs = [(1,0), (-1, 0), (0, 1), (0, -1)]
        while q:
            r, c = q.popleft()

            for dr, dc in dirs:
                nr, nc =dr+r, dc+c

                if nr<0 or nr>=rows or nc<0 or nc>=cols or grid[nr][nc]==- 1 or (nr, nc) in visit:
                    continue

                grid[nr][nc] = grid[r][c]+1
                visit.add((nr, nc))
                q.append((nr, nc))
        