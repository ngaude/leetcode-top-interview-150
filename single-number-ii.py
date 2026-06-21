from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0
        for num in nums:
            # Update twos: add bits from ones that are also in num
            twos |= ones & num
        
            # Update ones: XOR with num to toggle bits
            ones ^= num
        
            # Clear bits that have appeared three times
            # (bits that are in both ones and twos)
            threes = ones & twos
            ones &= ~threes
            twos &= ~threes
    
        return ones