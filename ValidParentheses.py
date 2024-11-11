class Solution(object):
    def isValid(self, s):
        char = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for c in s:
            if c in char:   # push to stack if value is opening char
                stack.append(c)
            elif c in char.values():    # char is closing char
                # if stack is empty or ToS is not the matching pair, return False
                if not stack or char[stack.pop()] != c:
                    return False
        # True if stack is empty, False otherwise
        return True if not stack else False
