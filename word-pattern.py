class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        n = len(pattern)
        d = {}
        used = set()
        words = s.split()
        if len(words) != n:
            return False
        for i in range(n):
            w = words[i]
            c = pattern[i]
            if w in d:
                if d[w] != c:
                    return False
            else:
                if c in used:
                    return False
                d[w] = c
                used.add(c)
        return True
    
pattern = "abba"
s = "dog cat cat dog"
assert Solution().wordPattern(pattern,s) == True


pattern = "aaaa"
s = "dog cat cat dog"
assert Solution().wordPattern(pattern,s) == False