class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            elif c == ')':
                if len(stack) and stack[-1] == '(':
                    stack.pop()
                else:
                    return False    
            elif c == ']':
                if len(stack) and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif c == '}':
                if len(stack) and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

assert Solution().isValid("()") == True
assert Solution().isValid("()[]{}") == True
assert Solution().isValid("(]") == False
assert Solution().isValid("([])") == True
assert Solution().isValid("([)]") == False

            
            
