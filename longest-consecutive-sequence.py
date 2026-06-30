from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        lc = 0
        for num in nums:
            if num not in d:
                a = d[num-1][0] if num-1 in d else num
                b = d[num+1][1] if num+1 in d else num
                d[num] = (a,b)
                d[a] = (a,b)
                d[b] = (a,b)
                if lc < b-a+1:
                    lc = b-a+1
        return lc

nums = [100,]
assert Solution().longestConsecutive(nums) == 1

nums = [100,102]
assert Solution().longestConsecutive(nums) == 1

nums = [100,101]
assert Solution().longestConsecutive(nums) == 2


nums = [100,4,200,1,3,2]
assert Solution().longestConsecutive(nums) == 4

import random
nums = list(range(100))
random.shuffle(nums)
assert Solution().longestConsecutive(nums) == len(nums)