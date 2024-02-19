# 200/212 - Passed

from typing import List


def maxProfit(prices: List[int]) -> int:
    left_index = 0
    right_index: int = 1
    current_max = 0

    while right_index < len(prices):
        if prices[right_index] > prices[left_index]:
            current_max = max(current_max, prices[right_index] - prices[left_index])

        else:
            temp = right_index
            right_index += 1
            left_index = temp
            continue
        right_index += 1

    return current_max


test_value = maxProfit([3, 2, 6, 5, 0, 3])
print(test_value)
