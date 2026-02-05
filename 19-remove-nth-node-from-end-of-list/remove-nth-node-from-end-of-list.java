/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode a=head;
        while(n-->0)a=a.next;
        ListNode b=head;
        if(a==null)return head.next;
        while(a.next!=null){
            b=b.next;a=a.next;
        }
        b.next=b.next.next;
        return head;
    }
}