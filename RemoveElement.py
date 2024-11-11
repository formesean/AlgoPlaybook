class Solution(object):
    def removeElement(self, nums, val):
        i = 0

        while i < len(nums):
            if nums[i] == val:
                nums.pop(i) # remove from the array if current num is equal to val
            else:
                i += 1  # move to next index

        return len(nums) # new length of nums array
