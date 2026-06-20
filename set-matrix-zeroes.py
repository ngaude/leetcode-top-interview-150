from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        m = len(matrix)
        n = len(matrix[0]) 

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 0
        
        return

matrix = [[1,1,1],[1,0,1],[1,1,1]]
res = [[1,0,1],[0,0,0],[1,0,1]]
Solution().setZeroes(matrix)
assert matrix== res
 
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
res = [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
Solution().setZeroes(matrix)
assert matrix== res
