class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:    # if empty, no common prefix
            return ""

        prefix = strs[0]    # starts at first str in strs

        for s in strs[1:]: # iterate starting at the 2nd index
            # shortens prefix until it matches the current str
            while s[:len(prefix)] != prefix:
                prefix = prefix[:-1]    # remove the last char

            if not prefix:  # if empty, return empty str
                return ""

        return prefix
