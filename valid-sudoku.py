from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check lines
        for i in range(9):
            nums = [int(board[i][j]) for j in range(9) if board[i][j] != '.']
            if len(set(nums)) != len(nums):
                return False 
        # check columns
        for i in range(9):
            nums = [int(board[j][i]) for j in range(9) if board[j][i] != '.']
            if len(set(nums)) != len(nums):
                return False 
        # check blocks
        combinations = [(i,j) for i in range(3) for j in range(3)]
        for i,j in combinations:
            nums = [int(board[i*3+x][j*3+y]) for x,y in combinations if board[i*3+x][j*3+y] != '.']
            if len(set(nums)) != len(nums):
                return False 
        return True

board = \
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
res = Solution().isValidSudoku(board)
print(res)

board = \
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
res = Solution().isValidSudoku(board)
print(res)
