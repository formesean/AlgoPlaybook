import itertools

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xb = bin(x)[2:]
        yb = bin(y)[2:]
        res = 0

        for a, b in itertools.zip_longest(xb[::-1], yb[::-1], fillvalue="0"):
            if a != b:
                res += 1

        return res
