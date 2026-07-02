class Solution:
    def maxAdjacentDistance(self, nums):
        ans = 0
        n = len(nums)

        for i in range(n):
            ans = max(ans, abs(nums[i] - nums[(i + 1) % n]))

        return ans