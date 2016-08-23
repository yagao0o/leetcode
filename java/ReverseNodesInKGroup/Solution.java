package ReverseNodesInKGroup;
import Helper.*;

import java.util.List;

/**
 * Created by Luyz on 16/8/23.
 * https://leetcode.com/problems/reverse-nodes-in-k-group/
 */
public class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode leftFlag = new ListNode(0);
        ListNode currentTotal = leftFlag;
        ListNode newGroupHeader = new ListNode(0);
        ListNode currentGroupNode = null;
        int groupSize = 0;
        while (head != null){
            ListNode currentNode = head;
            head = head.next;
            currentNode.next = newGroupHeader.next;
            newGroupHeader.next = currentNode;
            groupSize += 1;
            if (groupSize == 1){
                currentGroupNode = newGroupHeader.next;
            }
            if (groupSize == k){
                currentTotal.next = newGroupHeader.next;
                currentTotal = currentGroupNode;
                newGroupHeader.next = null;
                currentGroupNode = null;
                groupSize = 0;
            }
        }
        ListNode current = newGroupHeader.next;
        while (current!=null){
            ListNode node = current;
            current = current.next;
            node.next = currentTotal.next;
            currentTotal.next = node;
        }
        return leftFlag.next;
    }
}