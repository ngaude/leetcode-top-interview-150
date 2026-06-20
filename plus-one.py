from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        i = 0
        res = []
        inc = 1
        for d in  digits[::-1]:
            v = d+inc+carry
            res.append(v%10)
            carry = v//10
            inc = 0
        if carry>0:
            res.append(1)
        res = res[::-1]
        return res


digits = [1,2,3]
output = [1,2,4]
assert Solution().plusOne(digits) == output
digits = [4,3,2,1]
output = [4,3,2,2]
assert Solution().plusOne(digits) == output
digits = [9]
output = [1,0]
assert Solution().plusOne(digits) == output