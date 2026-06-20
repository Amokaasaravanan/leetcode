class Solution:
    def minOperations(self, nums, k):
        count = 0

        for num in nums:
            if num < k:
                count += 1

        return count