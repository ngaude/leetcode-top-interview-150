from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        n = len(gas)
        i = n - 1
        j = n - 1
        cnt = 0
        tank = 0
        while cnt < n:
            tank += gas[j] - cost[j]
            j = (j+1) % n
            cnt += 1
            while tank < 0 and cnt < n:
                i -=1
                tank += gas[i] - cost[i]
                cnt += 1
                        
        if tank >= 0:
            return i
        
        return -1
        

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
assert Solution().canCompleteCircuit(gas,cost)==3
print('---')
gas = [2,3,4]
cost = [3,4,3]
assert Solution().canCompleteCircuit(gas,cost)==-1