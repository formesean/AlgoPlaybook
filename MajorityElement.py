class Solution(object):
    def majorityElement(self, nums):
        x = len(nums) // 2
        dic = {}

        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        for key, value in dic.items():
            if value > x:
                return key

