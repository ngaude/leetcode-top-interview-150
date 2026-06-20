class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if x == 1:
            return 1
        if x == -1:
            if n&1:
                return -1
            else:
                return 1
        res = 1
        if n == 0:
            return res
        elif n>0:
            while n>0 and res:
                res *= x
                n-=1
        else:
            while n<0 and res:
                res /= x
                n+=1
        return res