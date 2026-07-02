class Solution:
    def countPartitions(self, nums):
        if sum(nums) % 2 != 0:
            return 0
        return len(nums) - 1