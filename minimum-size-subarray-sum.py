from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)
        if s < target:
            return 0
        if s == target:
            return n
        start = 0
        end = 0
        s = nums[0]
        res = n
        while True:
            if s < target:
                if end >= n - 1:
                    break
                end +=1
                s+= nums[end]
            if s >= target:
                if end - start < res:
                    res = end - start + 1
                    print(nums[start:end+1],sum(nums[start:end+1]),'res=',res)
                    
                s-= nums[start]
                start +=1
        return res
    

nums = [12,28,83,4,25,26,25,2,25,25,25,12]
target = 213
output = 8
res = Solution().minSubArrayLen(target, nums)
assert res == output

target = 4
nums = [1,4,4]
output = 1
res = Solution().minSubArrayLen(target, nums)
assert res == output

target = 11
nums = [1,1,1,1,1,1,1,1]
output = 0
res = Solution().minSubArrayLen(target, nums)
assert res == output

target = 11
nums = [1,2,3,4,5]
output = 3
res = Solution().minSubArrayLen(target, nums)
assert res == output