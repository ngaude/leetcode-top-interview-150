from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = sorted(nums)
        pos = len(s)//2
        return s[pos]

nums = [2,2]
res = Solution().majorityElement(nums)
print(res)