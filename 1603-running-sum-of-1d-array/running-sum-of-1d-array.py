class Solution:
    def runningSum(self, nums):
      sum=0
      result=[]
      for i in nums:
           sum+=i
           result.append(sum)
      return  result