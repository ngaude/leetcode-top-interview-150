from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        row_min = 0
        row_max = m-1
        col_min = 0
        col_max = n-1
        res = []
        while row_min <= row_max and col_min <= col_max:
            # topline
            res += [matrix[row_min][col] for col in range(col_min,col_max+1)]
            row_min += 1
            # rightline
            res += [matrix[row][col_max] for row in range(row_min,row_max+1)]
            col_max -= 1
            # bottomline
            if row_min <= row_max:
                res += [matrix[row_max][col] for col in range(col_max,col_min-1,-1)]
                row_max -= 1
            # leftline
            if col_min <= col_max:
                res += [matrix[row][col_min] for row in range(row_max,row_min-1,-1)]
                col_min += 1
        return res

matrix = [[6,9,7]]
assert Solution().spiralOrder(matrix) == [6,9,7]

matrix = [[1,2,3],[4,5,6],[7,8,9]]
assert Solution().spiralOrder(matrix) == [1,2,3,6,9,8,7,4,5]

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
assert Solution().spiralOrder(matrix) == [1,2,3,4,8,12,11,10,9,5,6,7]
