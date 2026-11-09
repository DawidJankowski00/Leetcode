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
    public ListNode Partition(ListNode head, int x)
    {
        ListNode l = new ListNode();
        ListNode r = new ListNode();
        ListNode lt = l;
        ListNode rt = r;


        while (head != null)
        {
            if (head.val >= x)
            {
                rt.next = new ListNode(head.val);
                rt = rt.next;
            }
            else
            {
                lt.next = new ListNode(head.val);
                lt = lt.next;
            }
            head = head.next;
        }

        lt.next = r.next;
        return l.next;
    }
}
