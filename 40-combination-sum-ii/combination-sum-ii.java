class Solution {
    List<List<Integer>> ans = new ArrayList<>();

    void backtrack(int[] arr, List<Integer> curr, int target, int idx) {
        if (target == 0) {
            ans.add(new ArrayList<>(curr));
            return;
        }

        if (target < 0 || idx == arr.length) return;

        // pick
        curr.add(arr[idx]);
        backtrack(arr, curr, target - arr[idx], idx + 1);
        curr.remove(curr.size() - 1);

        // skip duplicates
        while (idx + 1 < arr.length && arr[idx] == arr[idx + 1]) {
            idx++;
        }

        // not pick
        backtrack(arr, curr, target, idx + 1);
    }

    public List<List<Integer>> combinationSum2(int[] arr, int target) {
        Arrays.sort(arr);
        backtrack(arr, new ArrayList<>(), target, 0);
        return ans;
    }
}