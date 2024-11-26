from typing import List

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        evens = sorted([nums[i] for i in range(len(nums)) if i % 2 == 0])
        odds = sorted([nums[i] for i in range(len(nums)) if i % 2 == 1], reverse=True)
        res = []
        e, o = 0, 0

        for i in range(len(nums)):
            if i % 2 == 0:
                res.append(evens[e])
                e += 1
            else:
                res.append(odds[o])
                o += 1

        return res
