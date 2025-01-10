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
    public ListNode ReverseKGroup(ListNode head, int k)
    {
        var tmp = new int[k];
        for (int i = 0; i < k; i++)
            tmp[i] = 0;
        ListNode curr = head;
        ListNode st = head;
        bool test = false;
        while (curr != null)
        {
            for (int i = 0; i < k; i++)
            {
                tmp[i] = curr.val;
                curr = curr.next;
                if (curr == null && i < k - 1)
                {
                    test = true;
                    break;
                }
            }
            if (test)
                break;
            for (int i = 1;i < k+1; i++)
            {
                st.val = tmp[^i];
                st = st.next;
            }
        }
        return head;
    }
}
