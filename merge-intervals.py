from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals = sorted(intervals,key = lambda x: x[0])
        l = []
        a,b = intervals[0]
        for c,d in intervals[1:]:
            if c > b:
                l.append([a,b])
                a,b = c,d
            elif c == b:
                b = d
            else:
                b = max(b,d)
        l.append([a,b])
        return l
 

intervals = [[1,3],[2,6],[8,10],[15,18]]
res = Solution().merge(intervals)
assert res == [[1,6],[8,10],[15,18]]

intervals = [[1,4],[4,5]]
res = Solution().merge(intervals)
assert res == [[1,5]]

intervals = [[4,7],[1,4]]
res = Solution().merge(intervals)
assert res == [[1,7]]

intervals = [[1,4],[4,12],[9,27] ]
res = Solution().merge(intervals)
assert res == [[1,27]]
