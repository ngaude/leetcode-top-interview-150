from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a = Counter(s)
        b = Counter(t)
        return a==b

s = "anagram"
t = "nagaram"
assert Solution().isAnagram(s,t) == True

s = "rat"
t = "car"
assert Solution().isAnagram(s,t) == False

 