class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        s   = 0
        res = 0
        h   = {0: 1}   
        for num in nums:
            s += num                      

            res += h.get(s - k, 0)        

            h[s] = h.get(s, 0) + 1       

        return res