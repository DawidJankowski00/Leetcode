using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public class ListNode
{
    public int val;
    public ListNode next;
    public ListNode(int val = 0, ListNode next = null)
    {
        this.val = val;
        this.next = next;
    }
}

public class Solution {
    public ListNode DeleteMiddle(ListNode head) {
        if (head.next == null) return null;
        ListNode n = head;
        ListNode prev_middle = new ListNode(0, head);
        while (n.next != null)
        {
            n = n.next;
            prev_middle = prev_middle.next;
            if (n.next != null) n = n.next;
        }
        prev_middle.next = prev_middle.next.next;
        return head;
    }
}