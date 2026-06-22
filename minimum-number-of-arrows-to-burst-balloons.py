from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 2:
            return n 
        arrow = 0
        hit = 0
        points = sorted(points)
        curr = []
        curr_right_min = None
        for x,y in points:
            curr.append((x,y))
            if curr_right_min and x > curr_right_min:
                # shoot an arrow at curr_right_min...
                arrow += 1
                miss = [(_x,_y)for _x,_y in curr if _x > curr_right_min or _y < curr_right_min]
                hit += len(curr) - len(miss)
                curr = miss
            curr_right_min = min([_y for _,_y in curr])
        # finish to pop the remaining ballons
        while len(curr):
            curr_right_min = min([_y for _,_y in curr])
            # shoot an arrow at curr_right_min...
            arrow += 1
            miss = [(_x,_y)for _x,_y in curr if _x > curr_right_min or _y < curr_right_min]
            hit += len(curr) - len(miss)
            curr = miss
        return arrow
        

points = [[10,16],[2,8],[1,6],[7,12]]
assert Solution().findMinArrowShots(points)==2

points =  [[1,2],[2,3],[3,4],[4,5]]
assert Solution().findMinArrowShots(points)==2

points =  [[1,2],[3,4],[5,6],[7,8]]
assert Solution().findMinArrowShots(points)==4