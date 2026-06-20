from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k:
            nums[:] = nums[-k:] + nums[:-k]
l = [1,2,3,4,5,6]
Solution().rotate(l,3)
print(l)

        