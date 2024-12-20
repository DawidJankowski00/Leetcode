using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class TreeNode {
        public int val;
        public TreeNode left;
        public TreeNode right;
        public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public class Solution
    {
        public TreeNode ReverseOddLevels(TreeNode root)
        {
            void DFS(TreeNode nodel, TreeNode noder, int level)
            {
                if (nodel == null || noder == null)
                {
                    return;
                }
                if (level % 2 != 0)
                {
                    int temp = nodel.val;
                    nodel.val = noder.val;
                    noder.val = temp;
                }
                DFS(nodel.left, noder.right, level + 1);
                DFS(nodel.right, noder.left, level + 1);
            }
            DFS(root.left, root.right, 1);
            return root;
        }
    }
}

