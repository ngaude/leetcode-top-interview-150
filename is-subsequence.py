
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        si = 0
        ti = 0
        while si < len(s) and ti < len(t):
            if s[si] == t[ti]:
                si+=1
                ti+=1
            else:
                ti+=1
        return si == len(s)

# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true
s = "abc"
t = "ahbgdc"
assert Solution().isSubsequence(s,t) == True

# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false
s = "axc"
t = "ahbgdc"
assert Solution().isSubsequence(s,t) == False