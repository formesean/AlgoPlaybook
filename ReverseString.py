class Solution(object):
    def reverseString(self, s):
        l, r = 0, len(s)-1  # l = first index, r = last index

        while l < r:
            s[l], s[r] = s[r], s[l] # swap elements in indices
            l += 1  # move to left
            r -= 1  # move to right
