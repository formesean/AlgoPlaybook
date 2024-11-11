class Solution(object):
    def singleNumber(self, nums):
        hashmap = {}

        for n in nums:
            if n in hashmap:
                hashmap[n] += 1 # increment the frequency of the number
            else:
                hashmap[n] = 1 # add number to hashmap

        for key, value in hashmap.items():
            if value == 1:
                return key

        return None
