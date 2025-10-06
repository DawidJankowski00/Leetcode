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

public class Solution
{
    public ListNode DeleteDuplicates(ListNode head)
    {
        ListNode dummy = new ListNode(-1, head);
        ListNode prev = dummy;
        ListNode curr = head;

        while (curr != null && curr.next != null)
        {
            if (curr.val == curr.next.val)
            {
                while (curr.next != null && curr.val == curr.next.val) curr = curr.next;
                prev.next = curr.next;
            }
            else
            {
                prev = prev.next;
            }
            curr = curr.next;
        }

        return dummy.next;
    }
}
