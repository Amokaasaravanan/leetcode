class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        return min(((cap, i) for i, cap in enumerate(capacity) if cap >= itemSize), default=(-1, -1))[1]