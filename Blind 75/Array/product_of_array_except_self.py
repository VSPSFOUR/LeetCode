from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        cummlative_product = 1
        new_arr  = list(range(len(nums)))
        for i in range(len(nums)):
            new_arr[i] = cummlative_product
            cummlative_product*=nums[i]
        print(new_arr)
        cummlative_product = 1
        for j in range(len(nums) -1 , -1, -1):
            new_arr[j] *= cummlative_product
            cummlative_product *= nums[j]
            
            
        return new_arr