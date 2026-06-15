# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        n=0
        curr=head

        while curr:
            n+=1
            curr=curr.next
        curr=head

        for _ in range(n // 2-1):
            curr = curr.next
        curr.next = curr.next.next

        return head