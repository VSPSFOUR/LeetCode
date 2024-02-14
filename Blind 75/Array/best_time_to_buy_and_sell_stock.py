# 200/212 - Passed

from typing import List
def maxProfit( prices: List[int]) -> int:
#     max_dif = 0
#     for i in range(len(prices)):
#         start_day = prices[i]
#         smallest_left_most = True
#         for j in range(1 + i , len(prices)):
#             end_day = prices[j]
#             if(start_day > end_day):
#                 smallest_left_most = False
#             dif = end_day - start_day
#             if(dif > max_dif):
#                 max_dif = dif 
#         if(smallest_left_most):
#             return max_dif
        
#     return max_dif
                
        
    # left_pointer = 0 
    # right_pointer = len(prices) -1 

    # left_min = prices[left_pointer]
    # right_max = prices[right_pointer]
    
    # while(left_pointer <= right_pointer and left_pointer < len(prices) and right_pointer > 0):

    #     left_value = prices[left_pointer]
    #     right_value = prices[right_pointer]
    #     if(left_value < left_min):
    #         left_min = left_value
    #     if(right_value > right_max):
    #         right_max =right_value
    #     left_pointer += 1
    #     right_pointer -= 1
    # print("L :", left_min)
    # print("R : ", right_max)
    # differance = right_max  - left_min
    # if(differance < 0):
    #     return 0
    # return right_max - left_min
    
    left = 0
    right = 1
    max_diff = 0
    while( right < len(prices)):
        left_value = prices[left]
        right_value = prices[right]
        
        diff = right_value - left_value
        if(diff < 0):
            left  = right
            right += 1 
            continue
        if(diff > max_diff):
            max_diff = diff
            left = right
            right += 1 
            continue 
        if(diff > 0):
            right += 1
            continue
    return max_diff
            
        
test_value = maxProfit([3,2,6,5,0,3])
print(test_value)