class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        t = []
        while x > 0:
            t.append(x%10)
            x = x//10
        return t == t[::-1]

assert Solution().isPalindrome(121)==True
