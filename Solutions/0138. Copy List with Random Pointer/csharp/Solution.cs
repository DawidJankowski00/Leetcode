using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Linq;

public class Node
{
    public int val;
    public Node next;
    public Node random;
    public Node(int val = 0)
    {
        val = val;
        next = next;
        random = null;
    }
}

public class Solution
{
    public Node CopyRandomList(Node head)
    {
        if (head == null)
            return null;
        Node curr = head;
        Dictionary<Node, Node> cop = new Dictionary<Node, Node>();
        while (curr != null)
        {
            cop[curr] = new Node(curr.val);
            curr = curr.next;
        }
        curr = head;
        while (curr != null)
        {
            cop[curr].next = curr.next != null ? cop[curr.next] : null;
            cop[curr].random = curr.random != null ? cop[curr.random] : null;    
            curr = curr.next;
        }
        return cop[head];
    }
}
