class Solution:
    def captureForts(self, forts):
        ans = 0
        prev = -1

        for i in range(len(forts)):
            if forts[i] != 0:        
                if prev != -1 and forts[i] != forts[prev]:
                    ans = max(ans, i - prev - 1)
                prev = i

        return ans