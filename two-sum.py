from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def argsort(seq):
            return sorted(range(len(seq)), key=seq.__getitem__)

        idx = argsort(nums)
        for i in range(len(idx)-1):
            for j in range(i+1,len(idx)):
                if nums[idx[i]]+nums[idx[j]] == target:
                    return [idx[i],idx[j]]
