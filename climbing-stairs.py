d = {}
d[0]=0
d[1]=1
d[2]=2

class Solution:
    def climbStairs(self, n: int) -> int:
        res = 0
        if n in d:
            return d[n]
        res += self.climbStairs(n-1) + self.climbStairs(n-2)
        d[n]=res
        return res
    
assert Solution().climbStairs(2) == 2
assert Solution().climbStairs(3) == 3
