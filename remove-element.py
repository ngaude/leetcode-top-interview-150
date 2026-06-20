from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for j in range(len(nums)):
            nums[j-k] = nums[j]
            if nums[j] == val:
                k += 1
        print(j,k)
        return j+1-k

nums = [0,0,0,0,0,0,0]
res = Solution().removeElement(nums,0)
print(res,nums)