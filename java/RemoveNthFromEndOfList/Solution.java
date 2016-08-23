package RemoveNthFromEndOfList;

import Helper.*;

/**
 * Created by Luyz on 16/8/23.
 * https://leetcode.com/problems/remove-nth-node-from-end-of-list/
 */
public class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode left = new ListNode(0);
        left.next = head;
        ListNode current = head;
        int total = 0;
        while (current != null){
            total += 1;
            current = current.next;
        }
        int fromBegin = total - n;
        current = left;
        for (int i = 0; i < fromBegin; i++) {
            current = current.next;
        }
        current.next = current.next.next;
        return left.next;
    }
}
