from typing import List

class Solution:
    def jump(self, nums: List[int]) -> bool:
        n = len(nums)
        c = [10000]*n
        c[0] = 0
        for i in range(n):
            for j in range(1,nums[i]+1):
                if i+j < n:
                    cc = c[i]+1
                    if cc < c[i+j]:
                        c[i+j] = cc
        return c[-1]

nums = [2,3,1,1,4]
res = Solution().jump(nums)
assert res == 2

nums = [2,3,0,1,4]
res = Solution().jump(nums)
assert res == 2

nums = [1,2]
res = Solution().jump(nums)
assert res == 1
