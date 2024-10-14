class Solution(object):
    def twoSum(self, nums, target):
        di={}
        for i in range(len(nums)):
            if not target-nums[i] in di:
                di[nums[i]]=i
            else:
                return i,di[target-nums[i]]