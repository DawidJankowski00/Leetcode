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

    public class BSTIterator
    {
        List<int> tab;
        int curr = 0;
        public List<int> dfs(TreeNode node)
        {
            if(node == null) return new List<int>();
            var l1 = dfs(node.left);
            l1.Add(node.val);
            l1.AddRange(dfs(node.right));
            return l1;
        }
        public BSTIterator(TreeNode root)
        {
            tab = dfs(root);
        }

        public int Next()
        {
            curr++;
            return tab[curr-1];
        }

        public bool HasNext()
        {
            return curr < tab.Count; 
        }
    }
}
