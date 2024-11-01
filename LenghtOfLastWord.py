class Solution(object):
    def lengthOfLastWord(self, s):
        isSpace = True
        res = 0

        for char in s:
            if char != " ":
                res = 1 if isSpace else res + 1
                isSpace = False
            else:
                isSpace = True

        return res
        
