from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = {}
        k = 0
        for i in range(len(nums)):
            c = d.get(nums[i],0)
            if c < 2 :
                nums[k] = nums[i]
                d[nums[i]] = c+1
                k += 1    
        return k

nums = [0,1,1,0,0,7,0,7]
res = Solution().removeDuplicates(nums)
print(res, nums)