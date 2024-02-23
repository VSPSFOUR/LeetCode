# class Solution:
def hammingWeight(n: int) -> int:
    
    return str(n[2:]).count("1")

print(hammingWeight(0b11111111111111111111111111111101))