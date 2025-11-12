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
        public TreeNode DeleteNode(TreeNode root, int key)
        {
            if (root == null) return null;

            if (key < root.val)
            {
                root.left = DeleteNode(root.left, key);
            }
            else if (key > root.val)
            {
                root.right = DeleteNode(root.right, key);
            }
            else
            {
                if (root.left == null && root.right == null)
                {
                    return null;
                }
                else if (root.left != null)
                {
                    int predecessorVal = FindPredecessor(root.left);
                    root.val = predecessorVal;
                    root.left = DeleteNode(root.left, predecessorVal);
                }
                else
                {
                    int successorVal = FindSuccessor(root.right);
                    root.val = successorVal;
                    root.right = DeleteNode(root.right, successorVal);
                }
            }
            return root;
        }
        
        private int FindPredecessor(TreeNode node) 
        {
            while (node.right != null) 
                node = node.right;
            return node.val;
        }

        private int FindSuccessor(TreeNode node) 
        {
            while (node.left != null) 
                node = node.left;
            return node.val;
        }
    }
}
