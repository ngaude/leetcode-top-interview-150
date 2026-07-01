from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def cnk(n,k,i):
            if k == 0:
                yield []
            else:
                for j in range(i+1,n+1):
                    for e in cnk(n,k-1,j):
                        yield [j] + e
            return
        l = cnk(n,k,0)
        return list(l)

expected = [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]   
output = Solution().combine(4,2)
assert sorted(expected) == sorted(output)
