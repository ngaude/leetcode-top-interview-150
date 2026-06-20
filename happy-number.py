from typing import List

class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        l = [n]
        while True:
            num = 0
            for c in str(n):
                num += int(c)**2
            if num in l:
                return False
            elif num == 1:
                return True
            else:
                l.append(num)
                n = num
            print(l)

res = Solution().isHappy(19)
print(res)

res = Solution().isHappy(13453459)
print(res)


res = Solution().isHappy(2)
print(res)