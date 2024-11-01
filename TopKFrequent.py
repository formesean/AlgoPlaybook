class Solution(object):
    def topKFrequent(self, nums, k):
        seen = {}

        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1

        isSorted = sorted(seen.items(), key=lambda x: x[1], reverse=True)
        res = [key for key, value in isSorted]

        return res[:k]
