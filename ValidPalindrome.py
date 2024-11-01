import re

class Solution(object):
    def isPalindrome(self, s):
        if s == " ":
            return True

        s = re.sub(r'[^A-Za-z0-9]', "", s).lower()
        print(s)
        return s == s[::-1]
        
