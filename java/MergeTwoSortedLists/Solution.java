package MergeTwoSortedLists;
import Helper.*;

/**
 * Created by Luyz on 16/8/23.
 * https://leetcode.com/problems/merge-two-sorted-lists/
 */

public class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0);
        ListNode current = head;
        while (l1 != null && l2 != null){
            if (l1.val < l2.val){
                current.next = l1;
                l1 = l1.next;
            }
            else {
                current.next = l2;
                l2 = l2.next;
            }
            current = current.next;
        }
        if (l1 == null){
            current.next = l2;
        }
        if (l2 == null){
            current.next = l1;
        }
        return head.next;
    }
}
