from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row, col))
        
        while queue:
            r, c= queue.popleft()
            directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
            for row, col in directions:
                nr = r + row
                nc = c + col
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc]== 2**31 - 1:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))