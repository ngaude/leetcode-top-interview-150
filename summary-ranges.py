from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if len(nums) == 0:
            return res
        a = nums[0]
        b = nums[0]
        
        for i in range(1,len(nums)):
            if nums[i] > b+1:
                if a == b:
                    res.append(f"{a}")
                else:
                    res.append(f"{a}->{b}")
                a = nums[i]
                b = nums[i]
            else:
                b = nums[i]
        if a == b:
            res.append(f"{a}")
        else:
            res.append(f"{a}->{b}")
        return res

nums = [0,1,2,4,5,7]
res = Solution().summaryRanges(nums)
print(res)

nums = [0,2,3,4,6,8,9]
res = Solution().summaryRanges(nums)
print(res)
