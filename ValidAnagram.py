# Sorting
"""
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)
"""

# Hash Table
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        sCount, tCount = {}, {}

        for i in range(len(s)):
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
            tCount[t[i]] = 1 + tCount.get(t[i], 0)
        return sCount == tCount

