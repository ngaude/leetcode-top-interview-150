class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1:
            return 1
        low = 0
        high = x
        mid = x//2
        while True:
            mid = (high + low)//2
            xx = mid*mid
            if xx == x:
                break
            elif xx > x:
                if mid == high:
                    break
                high=mid
            else:
                if low == mid:
                    break
                low=mid
        return mid

Solution().mySqrt(1)

