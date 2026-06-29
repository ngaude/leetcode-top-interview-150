from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left = []
        lmax = 0
        right = []
        rmax = 0
        for i in range(len(height)):
            left.append(lmax)
            h = height[i]
            if h > lmax:
                lmax = h
            right.append(rmax)
            h = height[len(height)-1-i]
            if h > rmax:
                rmax = h
        right = right[::-1]
        rain = []
        for i in range(len(height)):
            r = max(min(right[i],left[i])-height[i],0)
            rain.append(r)
        # print('H',height)
        # print('L',left)
        # print('R',right)
        # print('=',rain)
        return sum(rain)

    def trap_naive(self, height: List[int]) -> int:
        def _fill(hh,left,right):
            border = min(left,right)
            if len(hh) == 0:
                return
            elif  max(hh) <= border:
                v = border * len(hh) - sum(hh)
                rain.append(v)
                return
            else:
                # trivial monotonic increase
                if left <= right:
                    monotonic = True
                    curr = left
                    for i in range(len(hh)):
                        if hh[i] < curr or hh[i] > right:
                            monotonic = False
                            break
                        curr = hh[i]
                    if monotonic:
                        return 0
                elif left >= right:
                    monotonic = True
                    curr = left
                    for i in range(len(hh)):
                        if hh[i] > curr or hh[i] < right:
                            monotonic = False
                            break
                        curr = hh[i]
                    if monotonic:
                        return 0
                # default
                hmax = -1
                hpos = -1
                for i in range(len(hh)):
                    if hh[i] > hmax:
                        hmax = hh[i]
                        hpos = i
                stack.append((hh[:hpos],left,hmax))
                stack.append((hh[(hpos+1):],hmax,right))
                return
            return
        
        if len(height) < 2:
            return 0
        rain = []
        stack = [(height[1:-1],height[0],height[-1])]
        while stack:
            hh,left,right = stack.pop()
            _fill(hh,left,right)
        return sum(rain)


height = [3,0,0,3]
assert Solution().trap(height) == 6


height = [0,1,0,2,1,0,1,3,2,1,2,1]
assert Solution().trap(height) == 6

height = [4,2,0,3,2,5]
assert Solution().trap(height) == 9

height = [5,4,1,2]
assert Solution().trap(height) == 1
