from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums = sorted([(val,pos) for pos,val in enumerate(nums)])
        i = 0 
        l = None
        curr = None
        for i in  range(len(nums)):
            val,pos = nums[i]
            if l is None:
                curr = val
                l = [pos]
            elif curr == val:
                l.append(pos)
            else:
                pos1 =l[0]
                for pos2 in l[1:]:
                    if pos2-pos1 <= k:
                        return True
                    pos1 = pos2
                curr = val
                l = [pos]
    
        if not l is None and len(l)>1:
            pos1 = l[0]
            for pos2 in l[1:]:
                if pos2-pos1 <= k:
                    return True
                pos1 = pos2
        return False

nums = [1,2,3,1]
k = 3
assert Solution().containsNearbyDuplicate(nums,k) == True

nums = [1,0,1,1]
k = 1
assert Solution().containsNearbyDuplicate(nums,k) == True

nums = [1,2,3,1,2,3]
k = 2
assert Solution().containsNearbyDuplicate(nums,k) == False

nums =[1,5,1,0]
k = 2
assert Solution().containsNearbyDuplicate(nums,k) == True
