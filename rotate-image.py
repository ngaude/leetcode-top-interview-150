from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for row in range(n//2):
            for i in range(0,n-row*2-1):
                top_left = matrix[row][row+i]
                top_right = matrix[row+i][n-1-row]
                bottom_right = matrix[n-1-row][n-1-row-i]
                bottom_left = matrix[n-1-row-i][row]
                matrix[row][row+i] = bottom_left
                matrix[row+i][n-1-row] = top_left
                matrix[n-1-row][n-1-row-i] = top_right
                matrix[n-1-row-i][row] = bottom_right
        return

matrix = [[1,2],[4,3]]
for i in matrix:
    print(i)
Solution().rotate(matrix)
print()
for i in matrix:
    print(i)
print()

matrix = [[1,2,3],[4,5,6],[7,8,9]]
res = [[7,4,1],[8,5,2],[9,6,3]]
for i in matrix:
    print(i)
Solution().rotate(matrix)
print()
for i in matrix:
    print(i)
assert matrix == res


matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
res = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
Solution().rotate(matrix)
assert matrix == res