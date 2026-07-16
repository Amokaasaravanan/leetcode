class Solution:
    def maxPower(self,s):
        count=1
        max=1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                count+=1
            else:
                count=1
            if count>max:
               max = count
        return max