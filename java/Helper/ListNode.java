package Helper;

/**
 * Created by Luyz on 16/8/19.
 */
public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int x) { val = x; }

    public void travel(){
        ListNode head = this;
        while (head != null){
            System.out.print(head.val + " ");
            head = head.next;
        }
        System.out.println("");
    }

    public static ListNode create(int[] intList){
        ListNode head = new ListNode(intList[0]);
        ListNode current = head;
        for (int i = 1; i < intList.length; i++) {
            ListNode newNode = new ListNode(intList[i]);
            current.next = newNode;
            current = newNode;
        }
        return head;
    }
}

