
from typing import List
from collections import deque

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        i1 = 0
        i2 = 0
        fifo = deque()

        for i1 in range(len(nums1)):
            if m > 0:
                fifo.append(nums1[i1])
                m += -1
            if len(fifo) > 0 and (i2>=n or fifo[0] <= nums2[i2]):
                nums1[i1] = fifo.popleft()
            else:
                nums1[i1] = nums2[i2]
                i2+=1

# a = [1,2,3,7,0,0,0]
# b = [4,5,8]
# Solution().merge(a,4,b,3)
# print('Solution',a)

# a = [2,0]
# m = 1
# b = [1]
# n = 1

a = [-1,0,0,3,3,3,0,0,0]
m = 6
b = [1,2,2]
n = 3

Solution().merge(a,m,b,n)
print(a)
