class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        count = 0
        def dfs(r, c):
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0<=nr and nr <rows and 0<=nc and nc<cols and grid[nr][nc]=="1":
                    if (nr,nc) not in visited:
                        visited.add((nr,nc))
                        dfs(nr, nc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r, c) not in visited:
                    dfs(r,c)
                    visited.add((r,c))
                    count+=1
        return count
                    