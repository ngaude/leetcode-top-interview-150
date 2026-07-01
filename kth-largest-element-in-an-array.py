from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pivot = nums[n//2]
        low = []
        high = []
        for num in nums:
            if num > pivot:
                high.append(num)
            elif num < pivot:
                low.append(num)
        npivot = n - len(high) - len(low)
        if k <= len(high):
            return self.findKthLargest(high,k)
        elif k <= len(high) + npivot:
            return pivot
        else:
            return self.findKthLargest(low,k - len(high)- npivot)


       
nums = [3,2,1,5,6,4]
assert Solution().findKthLargest(nums,2) == 5


nums = [3,2,3,1,2,4,5,5,6]
assert Solution().findKthLargest(nums,4) == 4
