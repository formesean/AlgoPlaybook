# Two Pointer Algorithm (works in positive integers only)
"""
class Solution(object):
    def twoSum(self, nums, target):
        indices = []
        left = 0
        right = len(nums) - 1

        for i in range(len(nums)):
            sum = nums[left] + nums[right]

            if sum == target:
                indices.append(left)
                indices.append(right)
                break
            elif sum > target:
                right -= 1
            else:
                left += 1
        return indices
"""


