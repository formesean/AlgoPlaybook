class Solution(object):
    def isValid(self, s):
        char = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for c in s:
            if c in char:
                stack.append(c)
            elif c in char.values():
                if not stack or char[stack.pop()] != c:
                    return False
        return True if not stack else False
        
