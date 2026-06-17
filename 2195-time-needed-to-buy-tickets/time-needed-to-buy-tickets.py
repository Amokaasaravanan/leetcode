class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        s, n = 0, tickets[k]
        for i, t in enumerate(tickets):
            if i <= k:
                s += min(n, t)
            else:
                s += min(n-1, t)
        return s