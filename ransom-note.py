class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = sorted(magazine)
        ransomNote = sorted(ransomNote)
        lm = len(magazine)
        lr = len(ransomNote)
        i=0
        j=0
        while i<lm and j<lr:
            j += (magazine[i] == ransomNote[j])
            i+=1
        return j == lr

assert Solution().canConstruct('a','b') == False
assert Solution().canConstruct('aa','ab') == False
assert Solution().canConstruct('aa','aab') == True