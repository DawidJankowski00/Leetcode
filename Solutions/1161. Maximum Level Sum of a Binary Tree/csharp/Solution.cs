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

    public class Solution {
        public int MaxLevelSum(TreeNode root) {
            int max_sum = int.MinValue;
            Queue<TreeNode> queue = new Queue<TreeNode>();
            queue.Enqueue(root);
            int result = 0;
            int curr = 1;
            while (queue.Count > 0)
            {
                int n = queue.Count;
                int tmp = 0;
                for (int i = 0; i < n; i++)
                {
                    TreeNode node = queue.Dequeue();
                    tmp += node.val;
                    if (node.left != null) queue.Enqueue(node.left);
                    if (node.right != null) queue.Enqueue(node.right);
                }
                if (tmp > max_sum)
                {
                    max_sum = tmp;
                    result = curr;
                }
                curr++;
            }
            return result;
        }
    }
}
