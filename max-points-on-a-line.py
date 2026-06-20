from typing import List

import math
from collections import Counter

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points)<3:
            return len(points)
        m = 0
        for x1,y1 in points:
            vecs = []
            for x2,y2 in points:
                if x1==x2 and y1==y2: 
                    continue
                dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
                if x2 > x1:
                    vec = ((x2-x1)/dist,(y1-y2)/dist)
                else:
                    vec = ((x1-x2)/dist,(y2-y1)/dist)
                vec = (round(vec[0],8),round(vec[1],8))
                vecs.append(vec)
            _m = max(Counter(vecs).values())+1
            print(Counter(vecs))
            if m < _m:
                m = _m
        return m

# points = [[1,1],[2,2],[3,3]]
# assert Solution().maxPoints(points) == 3

# points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# assert Solution().maxPoints(points) == 4

points = [[5151,5150],[0,0],[5152,5151]]
assert Solution().maxPoints(points) == 2