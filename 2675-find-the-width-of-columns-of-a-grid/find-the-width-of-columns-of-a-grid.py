class Solution:
    def findColumnWidth(self, grid):
        m = len(grid)
        n = len(grid[0])

        ans = []

        for col in range(n):
            maxi = 0

            for row in range(m):
                length = len(str(grid[row][col]))
                maxi = max(maxi, length)

            ans.append(maxi)

        return ans