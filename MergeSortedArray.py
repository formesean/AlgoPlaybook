class Solution(object):
    def merge(self, nums1, m, nums2, n):
        stack = []

        for num in range(m):
            stack.append(nums1[num])
        for num in range(n):
            stack.append(nums2[num])

        stack.sort()
        for i in range(len(stack)):
            nums1[i] = stack[i]
        return nums1
        
