class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        min_heap = [(grid[0][0], 0, 0)]

        visited = set()

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while min_heap:
            time, r, c = heapq.heappop(min_heap)

            if (r, c) in visited:
                continue

            visited.add((r, c))

            if r==n-1 and c==n-1:
                return time

            for dr, dc in dirs:
                nr = dr+r
                nc = dc+c

                if 0<=nr<n and 0<=nc<n:
                    if (nr, nc) not in visited:
                        new_time = max(time, grid[nr][nc])
                        heapq.heappush(min_heap, (new_time, nr, nc))