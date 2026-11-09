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
    public ListNode ReverseBetween(ListNode head, int left, int right)
    {
        ListNode curr = head;
        ListNode st = null;
        int[] tmp = new int[right-left+1];
        for (int i = 1; i < left; i++)
        {
            curr = curr.next;
        }
        st = curr;
        for (int i = 0; i < right - left + 1; i++)
        {
            tmp[i] = curr.val;
            curr = curr.next;
        }
        for (int i = 1;i < right-left+2; i++)
        {
            st.val = tmp[^i];
            st = st.next;
        }
        return head;
    }
}
