using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class ProductOfNumbers
    {
        private List<int> Stream;
        private int prod;

        public ProductOfNumbers()
        {
            Stream = new List<int>();
            prod = 1;
        }

        public void Add(int num)
        {
            if (num == 0)
            {
                Stream.Clear();
                prod = 1;
            }
            else
            {
                prod *= num;
                Stream.Add(prod);
            }
        }

        public int GetProduct(int k)
        {
            if (Stream.Count < k)
                return 0;
            if (Stream.Count == k)
                return Stream[^1];
            return Stream[^1] / Stream[^(k +1)];

        }
    }
}
