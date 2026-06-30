from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        print('\n'.join([str(r) for r in grid]))
        for i in range(1,m):
            grid[i][0] = grid[i-1][0] + grid[i][0]
        for j in range(1,n):
            grid[0][j] = grid[0][j-1] + grid[0][j]
        if m == 1 or n == 1:
            return grid[-1][-1]
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] = grid[i][j] + min(grid[i-1][j],grid[i][j-1])
        print('-'*n*3)
        print('\n'.join([str(r) for r in grid]))
        print()
        return grid[-1][-1]
        
grid = [[1,3,1],[1,5,1],[4,2,1]]
assert Solution().minPathSum(grid) == 7

grid = [[1,2,3],[4,5,6]]
assert Solution().minPathSum(grid) == 12