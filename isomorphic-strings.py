class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        m = {}
        mm = set()
        for i in range(len(s)):
            if s[i] in m:
                if m[s[i]] != t[i]:
                    return False
            else:
                if t[i] in mm:
                    return False
                m[s[i]] = t[i]
                mm.add(t[i])

        return True

s = "egg"
t = "add"
assert Solution().isIsomorphic(s,t) == True

s = "f11"
t = "b23"
assert Solution().isIsomorphic(s,t) == False

s = 'badc'
t = 'baba'
assert Solution().isIsomorphic(s,t) == False
