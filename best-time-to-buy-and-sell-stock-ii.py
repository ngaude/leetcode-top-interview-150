from typing import List

from collections import deque

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            p = prices[i] - prices[i-1]
            if p > 0:
                profit += p
        return profit


    
prices = prices = [7,1,5,3,6,4]
res = Solution().maxProfit(prices)
assert res == 7

prices = [1,2,3,4,5]
res = Solution().maxProfit(prices)
assert res == 4

prices = [7,6,4,3,1]
res = Solution().maxProfit(prices)
assert res == 0