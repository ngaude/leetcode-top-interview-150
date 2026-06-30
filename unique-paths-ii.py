from typing import List
from collections import deque

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        if m == 1 and n == 1:
            return 1
        grid = [[0]*n for i in range(m)]
        q = deque()
        q.append((0,0))
        # bfs
        visited = set()
        while q:

            i,j = q.popleft()
            if (i,j) in visited:
                continue
            visited.add((i,j))


            if obstacleGrid[i][j] == 1:
                grid[i][j] = 0
            else:
                if i == 0 and j == 0:
                    grid[i][j] = 1
                else:
                    up = grid[i-1][j] if i>=1 and obstacleGrid[i-1][j] == 0 else 0
                    left = grid[i][j-1] if j>=1 and obstacleGrid[i][j-1] == 0 else 0
                    grid[i][j] = up + left
                if i == m-1 and j == n-1:
                    break
                if i < m-1: 
                    q.append((i+1,j))
                if j < n-1: 
                    q.append((i,j+1))
            print(i,j,'=',q,grid[i][j])
            print('\n'.join([str(r) for r in grid]))
            print()
        print('\n'.join([str(r) for r in obstacleGrid]))
        print('-'*n*3)
        print('\n'.join([str(r) for r in grid]))
        return grid[-1][-1]


            


        print('\n'.join([str(r) for r in grid]))
        pass

obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
assert Solution().uniquePathsWithObstacles(obstacleGrid) == 2

obstacleGrid = [[0,1],[0,0]]
assert Solution().uniquePathsWithObstacles(obstacleGrid) == 1

obstacleGrid = [[0,0,0,0,0],[0,0,0,0,1],[0,0,0,1,0],[0,0,0,0,0]]
assert Solution().uniquePathsWithObstacles(obstacleGrid) == 10