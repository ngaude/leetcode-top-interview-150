from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i,num in enumerate(numbers):
            if num in d:
                return [d[num]+1,i+1]
            d[target-num] = i
        print(d)
        return

numbers = [2,7,11,15]
target = 9
res = Solution().twoSum(numbers,target)
print(res)
assert res == [1,2]