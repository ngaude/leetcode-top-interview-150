from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = {}
        k = 0
        for i in range(len(nums)):
            if nums[i] not in d:
                nums[k] = nums[i]
                d[nums[i]] = True
                k += 1    
        return k

nums = [0,1,1,0,7,0,7]
res = Solution().removeDuplicates(nums)
print(res, nums)