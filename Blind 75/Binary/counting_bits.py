from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = list(range(n+1))
        for i in range(n+1):
            ans[i] = i.bit_count() 
        
        return ans 
    
