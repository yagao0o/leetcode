package MergeKSortedList;
import Helper.*;
import java.util.*;
/**
 * Created by Luyz on 16/8/23.
 * https://leetcode.com/problems/merge-k-sorted-lists/
 */
public class Solution {
    // This way is better than the nextone
    public ListNode mergeKLists(ListNode[] lists) {
        int size = lists.length;
        if (size == 0){
            return null;
        }
        while (size > 1){
            boolean isOdd = size % 2 == 1;
            size = isOdd?(size + 1)/2:size/2;
            for (int i = 0; i < size - 1; i++) {
                lists[i] = mergeTwoLists(lists[2 * i], lists[2 * i + 1]);
            }
            if (isOdd){
                lists[size - 1] = lists[2 * size - 2];
            }
            else{
                lists[size - 1] = mergeTwoLists(lists[2 * size - 2], lists[2 * size - 1]);
            }
        }
        return lists[0];
    }

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


    public ListNode mergeKLists_2(ListNode[] lists) {
        ListNode header = new ListNode(0);
        ListNode current = header;
        ArrayList<ListNode> nodelist = new ArrayList<>();
        for (ListNode node: lists){
            insert(nodelist, node);
        }
        while (nodelist.size() > 0){
            ListNode node = nodelist.remove(0);
            current.next = node;
            current = current.next;
            insert(nodelist, node.next);
        }
        return header.next;
    }

    private void insert(ArrayList<ListNode> list, ListNode node){
        if (node == null){
            return;
        }
        int i = 0;
        while (i < list.size() && list.get(i).val < node.val){
            i ++;
        }
        list.add(i, node);
    }


}