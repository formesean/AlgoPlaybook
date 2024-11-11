class Solution(object):
    def removeDuplicates(self, nums):
        # uses in-place algorithm
        k = 1   # var to keep track of unique elements

        # iterate starting at the 2nd index
        for i in range(1, len(nums)):
            # if current element is not equal to the previous element
            if nums[i] != nums[i-1]:
                # assign the current element to the next unique element
                nums[k] = nums[i]
                k +=1

        return k
