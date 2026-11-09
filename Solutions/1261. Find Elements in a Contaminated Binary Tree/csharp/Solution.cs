using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class FindElements
    {
        Dictionary<int, bool> tab = new Dictionary<int, bool>();

        public FindElements(TreeNode root)
        {
            void rec(int x, TreeNode node)
            {
                if (node.left != null)
                {
                    int tmp = 2 * x + 1;
                    tab[tmp] = true;
                    rec(tmp, node.left);
                }
                if (node.right != null)
                {
                    int tmp = 2 * x + 2;
                    tab[tmp] = true;
                    rec(tmp, node.right);
                }
            }
            if (root != null)
            {
                tab[0] = true;
                rec(0, root);
            }
        }

        public bool Find(int target)
        {
            return tab.ContainsKey(target);
        }
    }
}
