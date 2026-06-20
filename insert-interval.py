from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        a,b = newInterval
        na = a
        nb = b
        rms = []
        for i,(x,y) in enumerate(intervals):
            if a <= x and y <= b:
                rms.append(i)
            if x <= a and a <= y:
                na = x
                rms.append(i)
            if x <= b and b <= y:
                nb = y
                rms.append(i)
        for i in sorted(set(rms))[::-1]:
            intervals.pop(i)
        intervals.append([na,nb])
        intervals.sort()
        return intervals




intervals = [[1,3],[6,9]]
newInterval = [2,5]
output = [[1,5],[6,9]]
Solution().insert(intervals,newInterval)
assert output == intervals

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
output = [[1,2],[3,10],[12,16]]
Solution().insert(intervals,newInterval)
assert output == intervals