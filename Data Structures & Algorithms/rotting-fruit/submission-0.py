from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        minutes = 0
        fresh = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==2:
                    queue.append((row, col))
                elif grid[row][col]==1:
                    fresh+=1

        if fresh == 0:
            return 0

        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        while queue and fresh > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if 0 <= nr and nr < rows and 0 <= nc and nc < cols:
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            fresh-=1
                            queue.append((nr, nc))
            minutes+=1
        if fresh > 0:
            return -1
        return minutes