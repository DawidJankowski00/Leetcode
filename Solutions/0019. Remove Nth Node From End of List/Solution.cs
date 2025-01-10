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
    public ListNode RemoveNthFromEnd(ListNode head, int n)
    {
        int c = 0;
        ListNode curr = head;
        while (curr != null)
        {
            c++;
            curr = curr.next;
        }
        if (c == n)
            return head.next;
        curr = head;
        for (int i = 0; i < c-n-1; i++)
            curr = curr.next;
        curr.next = curr.next.next;
        return head;
    }
}
