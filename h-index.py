from typing import List,Optional

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations)[::-1]
        h = 0
        for i,v in enumerate(citations):
            if v >= i+1:
                h = i+1
            else:
                break
        return h


citations = [3,0,6,1,5]
output = 3
res = Solution().hIndex(citations)
assert res == output

citations = [1,3,1]
output = 1
res = Solution().hIndex(citations)
assert res == output
        