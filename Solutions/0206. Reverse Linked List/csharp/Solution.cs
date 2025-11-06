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
    public ListNode ReverseList(ListNode head) {
        if (head == null) return head;
        ListNode prev = null;
        ListNode curr = head;
        ListNode next = head.next;
        while (next != null)
        {
            curr.next = prev;
            prev = curr;
            curr = next;
            next = next.next;
        }
        curr.next = prev;
        return curr;
    }
}
