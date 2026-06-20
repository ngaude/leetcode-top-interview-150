from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        mostWater = min(height[i],height[j])*(j-i)
        while i != j:
            if height[i] > height[j]:
                # move right pointer
                j = j - 1
            else:
                # move right pointer
                i = i + 1
            mostWater = max(mostWater,min(height[i],height[j])*(j-i))
        return mostWater

height = [1,8,6,2,5,4,8,3,7]
res = Solution().maxArea(height)
print(res)