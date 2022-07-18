from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m, n = len(grid), len(grid[0])

        grid.append(['0'] * len(grid[0]))
        for i in range(len(grid) - 1):
            grid[i].append('0')

        def expand_Islands(i, j):
            if grid[i][j] == "1":
                grid[i][j] = "0"

                expand_Islands(i + 1, j)
                expand_Islands(i, j + 1)
                expand_Islands(i - 1, j)
                expand_Islands(i, j - 1)

        island_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    island_count += 1
                    expand_Islands(i, j)

        return island_count