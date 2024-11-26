from typing import List

class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        bins = [bin(n)[2:] for n in nums]
        ml = max(len(b) for b in bins)
        bins = [b.zfill(ml) for b in bins]
        res = 0

        for i in range(ml):
            c = 0

            for b in bins:
                if b[i] == "1":
                    c += 1

            if c >= k:
                res |= (1 << (ml - 1 - i))

        return res
