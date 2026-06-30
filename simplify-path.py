class Solution:
    def simplifyPath(self, path: str) -> str:
        s = []
        for e in path.split('/'):
            if e == '..':
                if len(s):
                    s.pop()
            elif e == '.' or e == '':
                continue
            else:
                s.append(e)
        
        p = '/' + '/'.join(s)
        return p

path = "/home/"
assert Solution().simplifyPath(path) == "/home"

path = "/home//foo/"
assert Solution().simplifyPath(path) == "/home/foo"

path = "/home/user/Documents/../Pictures"
assert Solution().simplifyPath(path) == "/home/user/Pictures"

path = "/../"
assert Solution().simplifyPath(path) == "/"

path = "/.../a/../b/c/../d/./"
assert Solution().simplifyPath(path) == "/.../b/d"