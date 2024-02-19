from typing import List
class Solution:
    def containsDuplicate( nums: List[int]) -> bool:
        nums = sorted(nums)
        left_index = 0
        right_index = 1
        while(right_index < len(nums)):
            if(nums[left_index ] == nums[right_index]):
                return True 
            left_index = right_index 
            right_index += 1 
            
        return False