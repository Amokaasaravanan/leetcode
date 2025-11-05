  class Solution {
    public int uniquePaths(int m, int n) {
        if(m == 1 || n == 1) return 1;
        int[][] dp = new int[m][n];
        // for (int i = 0; i < m; i++) Arrays.fill(dp[i], -1);
        // return paths(m - 1, n - 1)
        // return memoization(m - 1, n - 1, dp);
        // return tabulation(m, n, dp);
        return tabulationSpaceOptimized(m, n);
    }

    public int paths(int i, int j) {
        if(i < 0 || j < 0) return 0;
        if(i == 0 && j == 0) return 1;
        return paths(i - 1, j) + paths(i, j - 1); // up + left
    }

    public int memoization(int i, int j, int[][] dp) {
        // TC : O(M * N)
        // SC : O((M - 1) + (N - 1)) + O(M * N)
        if(i < 0 || j < 0) return 0;
        if(i == 0 && j == 0) return 1;
        if (dp[i][j] != -1) return dp[i][j];
        return dp[i][j] = memoization(i - 1, j, dp) + memoization(i, j - 1, dp); // up + left
    }

    public int tabulation(int m, int n, int[][] dp) { //Stack optimized
        // TC : O(M * N)
        // SC : O(M * N)
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) dp[i][j] = 1;
                else {
                    int up = 0, left = 0;
                    if (i > 0) up = dp[i - 1][j];
                    if (j > 0) left = dp[i][j - 1];
                    dp[i][j] = up + left;
                }
            }
        }
        return dp[m - 1][n - 1];
    }

    public int tabulationSpaceOptimized(int m, int n) { 
        // TC : O(M * N)
        // SC : O(N)
        int[] dp = new int[n]; //Prev row of size number of columns
        for (int i = 0; i < m; i++) {
            int[] temp = new int[n];
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) temp[j] = 1;
                else {
                    int up = 0, left = 0;
                    if (i > 0) up = dp[j];
                    if (j > 0) left = temp[j - 1];
                    temp[j] = up + left;
                }
            }
            dp = temp;
        }
        return dp[n - 1];
    }
}