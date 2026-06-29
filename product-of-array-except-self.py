from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        fwd = [1]
        rwd = [1]
        for i in range(n):
            fwd.append(fwd[-1]*nums[i])
            rwd.append(rwd[-1]*nums[n-1-i])
        res = []
        for i in range(n):
            res.append(fwd[i]*rwd[n-i-1])
        return res

nums = [1,2,3,4]
output = [24,12,8,6]
res = Solution().productExceptSelf(nums)
assert res == output

nums = [-1,1,0,-3,3]
output = [0,0,9,0,0]
res = Solution().productExceptSelf(nums)
assert res == output
