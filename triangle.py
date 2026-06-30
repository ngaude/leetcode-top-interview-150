from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        a = [200*10000]*len(triangle[-1])
        a[0] = triangle[0][0]
        print(0,a,triangle[0])
        for i in range(1,len(triangle[-1])):
            mem = a[0]
            a[i] = a[i-1] + triangle[i][i]
            a[0] = a[0]+triangle[i][0]
            for j in range(1,i):
                val = min(mem,a[j]) + triangle[i][j]
                mem = a[j]
                a[j] = val
            print(i,a,triangle[i])
        return min(a)

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
assert Solution().minimumTotal(triangle) == 11

triangle = [[2],[3,4],[6,5,7],[4,1,8,3],[1,1,1,1,1]]
assert Solution().minimumTotal(triangle) == 12

triangle = [[1],[1,1],[1,2,1],[1,1,2,1],[1,2,2,2,1]]
assert Solution().minimumTotal(triangle) == 5