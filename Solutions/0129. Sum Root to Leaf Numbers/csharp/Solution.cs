using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int SumNumbers(TreeNode root) {
            int dfs(TreeNode node, int sum)
            {
                if (node == null) return 0;
                sum = sum * 10 + node.val;
                if (node.left == null && node.right == null) return sum;

                return dfs(node.left, sum) + dfs(node.right, sum);
            }
            return dfs(root, 0);
        }
    }
}
