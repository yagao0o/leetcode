package SwapNodesInPairs;

import Helper.*;
/**
 * Created by Luyz on 16/8/23.
 * https://leetcode.com/problems/swap-nodes-in-pairs/
 */
public class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode leftFlag = new ListNode(0);
        ListNode current = leftFlag;
        ListNode n1 = null;
        while (head != null){
            if (n1 == null){
                n1 = head;
                head = head.next;
            }
            else{
                ListNode n2 = head;
                head = head.next;

                current.next = n2;
                n2.next = n1;
                current = n1;
                n1.next = null;
                n1 = null;
            }
        }
        if (n1 != null){
            current.next = n1;
            n1.next = null;
        }
        return leftFlag.next;
    }
}