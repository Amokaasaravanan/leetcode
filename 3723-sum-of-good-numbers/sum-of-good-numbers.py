class Solution:
    def sumOfGoodNumbers(self, nums, k):
        total = 0
        n = len(nums)

        for i in range(n):
            good = True

            if i - k >= 0 and nums[i] <= nums[i - k]:
                good = False

            if i + k < n and nums[i] <= nums[i + k]:
                good = False

            if good:
                total += nums[i]

        return total