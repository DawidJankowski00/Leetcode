using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class TreeNode
    {
        public int val;
        public TreeNode left;
        public TreeNode right;
        public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null)
        {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public class Solution
    {
        public IList<IList<int>> ZigzagLevelOrder(TreeNode root)
        {
            if (root == null) return new List<IList<int>>();
            
            Queue<TreeNode> queue = new Queue<TreeNode>();
            queue.Enqueue(root);
            List<IList<int>> result = new List<IList<int>>();
            bool op = true;
            while (queue.Count > 0)
            {
                int l = queue.Count;
                List<int> tmp = new List<int>();
                for (int i = 0; i < l; i++)
                {
                    TreeNode node = queue.Dequeue();
                    tmp.Add(node.val);
                    if (node.left != null) queue.Enqueue(node.left);
                    if (node.right != null) queue.Enqueue(node.right);
                }
                if (op) 
                {
                    result.Add(tmp); 
                    op = false;
                }
                else
                {
                    tmp.Reverse();
                    result.Add(tmp);
                    op = true;
                }
            }
            return result;
        }
    }
}
