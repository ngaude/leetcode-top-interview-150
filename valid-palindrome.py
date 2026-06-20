class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c for c in s.lower() if c.isalnum()]
        return s == s[::-1]

s = "A man, a plan, a canal: Panama"
assert Solution().isPalindrome(s) == True

s = "race a car"
assert Solution().isPalindrome(s) == False
