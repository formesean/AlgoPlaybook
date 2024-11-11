class Solution(object):
    def strStr(self, haystack, needle):
        # if needle is empty, return 0
        if not needle:
            return 0

        for i in range(len(haystack)):  # iterate through the lenght of haystack
            # return index if substring matches needle
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1
