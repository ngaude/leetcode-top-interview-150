from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        o = [[c for c in row] for row in board]
        m = len(o)
        n = len(o[0]) 
        for i in range(m):
            for j in range(n):
                neighbors = [o[x][y] for x,y in [(i-1,j-1),
                                                (i-1,j),
                                                (i-1,j+1),
                                                (i,j-1),
                                                (i,j+1),
                                                (i+1,j-1),
                                                (i+1,j),
                                                (i+1,j+1)] if x>=0 and y>=0 and x<= m-1 and y<= n-1]
                s = sum(neighbors)
                if o[i][j] == 1:
                    if s < 2 or s >3:
                        board[i][j] = 0
                else:
                    if s == 3:
                        board[i][j] = 1

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
res = [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
Solution().gameOfLife(board)
assert board == res

board = [[1,1],[1,0]]
res = [[1,1],[1,1]]
Solution().gameOfLife(board)
assert board == res
