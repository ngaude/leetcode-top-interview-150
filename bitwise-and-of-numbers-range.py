class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        cnt = 0
        while left != right:
            cnt += 1
            left >>= 1
            right >>= 1
        return left << cnt
