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
        public int LongestZigZag(TreeNode root) {
            int result = 0;
            //True = last Left
            //False = last Right
            void dfs(TreeNode node, int curr, bool direction)
            {
                if (node == null)
                {
                    if (curr > result) result = curr;
                    return;
                }
                if (direction == null)
                {
                    dfs(node.left, 0, true);
                    dfs(node.right, 0, false);
                }
                else if (direction == true)
                {
                    dfs(node.left, 0, true);
                    dfs(node.right, curr+1, false);
                }
                else
                {
                    dfs(node.left, curr+1, true);
                    dfs(node.right, 0, false);
                }
            }
            dfs(root, 0, null);
            return result;
        }
    }
}
