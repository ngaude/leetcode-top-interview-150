from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        mem = {}
        def _rob(_i):
            if _i == 0:
                return nums[0]
            if _i == 1:
                return max(nums[0],nums[1])
            if _i in mem:
                return mem[_i]
            option1 = nums[_i] + _rob(_i-2)
            option2 = _rob(_i-1)
            best = max(option1,option2)
            mem[_i] = best
            return best
        
        return _rob(n-1)
        
nums = [1,2,3,1]
assert Solution().rob(nums) == 4

nums = [2,7,9,3,1]
assert Solution().rob(nums) == 12

nums = [226,174,214,16,218,48,153,131,128,17,157,142,88,43,37,157,43,221,191,68,206,23,225,82,54,118,111,46,80,49,245,63,25,194,72,80,143,55,209,18,55,122,65,66,177,101,63,201,172,130,103,225,142,46,86,185,62,138,212,192,125,77,223,188,99,228,90,25,193,211,84,239,119,234,85,83,123,120,131,203,219,10,82,35,120,180,249,106,37,169,225,54,103,55,166,124]
assert Solution().rob(nums) == 7102

nums = [1,2,1,1]
assert Solution().rob(nums) == 3
