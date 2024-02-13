class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            start_num = nums[i]
            rem_num = target - start_num
            try:
                rem_index = nums.index(rem_num) 
            except ValueError:
                continue
            if(rem_index != -1 and rem_index != i):
                return [i, rem_index]