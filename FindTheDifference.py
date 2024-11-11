class Solution(object):
    def findTheDifference(self, s, t):
        res = 0

        for c in s + t: # iterate over a combined str
            res ^= ord(c)   # XOR to check unique ASCII value

        return chr(res) # convert ASCII to char
