class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        stack = []

        for r in range(rows):
            for c in range(cols):
                area = 0
                if (r,c) not in visited and grid[r][c]==1:
                    directions = [[1,0], [-1,0], [0,1], [0,-1]]
                    area+=1
                    visited.add((r,c))
                    stack.append((r,c))
                    while stack:
                        node = stack.pop()
                        for dr, dc in directions:
                            nr, nc = node[0]+dr, node[1]+dc
                            if 0<=nr<rows and 0<=nc<cols:
                                if (nr, nc) not in visited and grid[nr][nc]==1:
                                    area+=1
                                    visited.add((nr,nc))
                                    stack.append([nr, nc])
                    max_area = max(area, max_area)
        
                    
                    



        return max_area