from typing import List

from collections import deque

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        buy = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] - buy > profit:
                profit = prices[i] - buy
            elif prices[i] <  buy:
                buy = prices[i]
        return profit
    
    def maxProfitNaive(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        if len(prices) == 2:
            if prices[0] < prices[1]:
                return prices[1] - prices[0]
            else:
                return 0
        profit = 0
        for i in range(len(prices) - 1):
            for j in range(i+1,len(prices)):
                if prices[j] - prices[i] > profit:
                    profit = prices[j] - prices[i]
        return profit

    
prices = [7,1,5,3,6,4]
res = Solution().maxProfit(prices)
assert res == 5

prices = [7,6,4,3,1]
res = Solution().maxProfit(prices)
assert res == 0

import random

for i in range(100):
    prices = [random.randint(0, 100) for j in range(3)]
    profitA = Solution().maxProfit(prices)
    profitB = Solution().maxProfitNaive(prices)
    print('>',prices,profitA,profitB)
    assert profitA == profitB

prices = [49, 17, 61]
res = Solution().maxProfit(prices)
