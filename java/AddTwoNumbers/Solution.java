package AddTwoNumbers;
import Helper.ListNode;

/**
 * Created by Luyz on 16/8/19.
 */
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0);
        ListNode currentNode = head;
        int current = 0;
        while (l1 != null && l2 != null){
            current += l1.val + l2.val;
            currentNode.next = new ListNode(current % 10);
            current = current / 10;
            currentNode = currentNode.next;
            l1 = l1.next;
            l2 = l2.next;
        }
        if (l1 == null){
            l1 = l2;
        }
        while (l1 != null) {
            current += l1.val;
            currentNode.next = new ListNode(current % 10);
            current = current / 10;
            currentNode = currentNode.next;
            l1 = l1.next;
        }
        if (current != 0){
            currentNode.next = new ListNode(current);
        }

        return head.next;
    }
}