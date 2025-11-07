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
    public int PairSum(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        while (fast != null && fast.next != null)
        {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode prev = null;
        ListNode nextnode = null;
        while (slow != null)
        {
            nextnode = slow.next;
            slow.next = prev;
            prev = slow;
            slow = nextnode;
        }
        int result = 0;
        while (prev != null)
        {
            int curr = head.val + prev.val;
            if (curr > result) result = curr;
            head = head.next;
            prev = prev.next;
        }
        return result;
    }
}
