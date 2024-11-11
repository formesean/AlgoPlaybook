class Solution(object):
    def isPalindrome(self, x):
        # converts int to str, reverse it, and check if it equals the original str
        return str(x) == "".join(reversed(str(x)))
        # returns True if equal, False otherwise
