# 200/212 - Passed

from typing import List
def maxProfit( prices: List[int]) -> int:
    max_dif = 0
    for i in range(len(prices)):
        start_day = prices[i]
        smallest_left_most = True
        for j in range(1 + i , len(prices)):
            end_day = prices[j]
            if(start_day > end_day):
                smallest_left_most = False
            dif = end_day - start_day
            if(dif > max_dif):
                max_dif = dif 
        if(smallest_left_most):
            return max_dif
        
    return max_dif
                
        
        
test_value = maxProfit([7,1,5,3,6,4])
print(test_value)