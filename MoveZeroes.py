class Solution(object):
    def moveZeroes(self, nums):
        for n in nums:
            if n == 0:
                nums.remove(n)
                nums.append(0)

        return nums
