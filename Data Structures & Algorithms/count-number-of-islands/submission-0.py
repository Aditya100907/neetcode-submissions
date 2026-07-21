class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        if not grid:
            return 0
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        def dfs (r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if (r,c) in visited or grid[r][c]=='0':
                return
            visited.add((r,c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c)
                    count+=1 
        return count          