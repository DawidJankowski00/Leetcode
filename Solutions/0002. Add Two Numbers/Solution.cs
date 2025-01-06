using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
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
        public ListNode AddTwoNumbers(ListNode l1, ListNode l2)
        {
            ListNode head = new ListNode(0);
            ListNode result = head;
            int carry = 0;
            while (l1 != null || l2 != null)
            {
                int l1val = l1 != null ? l1.val : 0;
                int l2val = l2 != null ? l2.val : 0;
                int tmp = carry + l1val + l2val;
                if (tmp >= 10)
                    carry = 1;
                else
                    carry = 0;
                ListNode newNode = new ListNode(tmp % 10);
                result.next = newNode;
                result = newNode;
                l1 = l1 != null ? l1.next : null;
                l2 = l2 != null ? l2.next : null;
            }
            return head.next;
        }
    }
}
