class Solution(object):
    def searchInsert(self, nums, target):
        count = 0
        for i in nums:
            if i < target:
                count += 1

        return count
        
