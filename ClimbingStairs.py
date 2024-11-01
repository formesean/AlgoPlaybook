class Solution(object):
    def climbStairs(self, n):
        a,b = 1, 1
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b
  
