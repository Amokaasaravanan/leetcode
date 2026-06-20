class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        result = len(nums)+1
        i = 0
        j = 0
        sum = 0
        while i < len(nums) :  
            sum = sum | nums[i]
            while sum >= k  and i>=j: 
                result = min(result, i-j+1)
                j+=1
                sum = 0
                for m in range(j,i+1):
                    sum = sum | nums[m]
            i+=1
        if result == len(nums)+1: return -1
        return result
            