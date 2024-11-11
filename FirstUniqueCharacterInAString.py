class Solution(object):
    def firstUniqChar(self, s):
        hm = {}

        for i in range(len(s)):
            curr = str(s[i])
            if curr in hm:
                hm[curr] += 1
            else:
                hm[curr] = 1
        print(hm)

        for i in range(len(s)):
            if hm[s[i]] == 1:
                return i
        return -1
