from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    queue.append((r,c))
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        while queue:
            node = queue.popleft()
            r, c = node[0], node[1]
            for dr, dc in directions:
                nr, nc = dr+r, dc+c
                if 0<= nr and nr < rows and 0<=nc and nc < cols:
                    if grid[nr][nc]==INF:
                        grid[nr][nc]=grid[r][c]+1
                        queue.append((nr, nc))

        