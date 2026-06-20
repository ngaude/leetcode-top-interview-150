class Solution:
    def trailingZeroes(self, n: int) -> int:
        z = 0
        i = 1
        while 5**i <= n:
            z += n//5**i
            i+=1
        return z

