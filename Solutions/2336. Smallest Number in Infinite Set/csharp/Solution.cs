using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class SmallestInfiniteSet
    {
        private int _minNum;
        private SortedSet<int> _addedBackNumbers;

        public SmallestInfiniteSet()
        {
            _minNum = 1;
            _addedBackNumbers = new SortedSet<int>();
        }

        public int PopSmallest()
        {
            if (_addedBackNumbers.Count > 0)
            {
                int smallest = _addedBackNumbers.Min;
                _addedBackNumbers.Remove(smallest);
                return smallest;
            }

            int result = _minNum;
            _minNum++;
            return result;
        }

        public void AddBack(int num)
        {
            if (num >= _minNum)
            {
                return;
            }

            _addedBackNumbers.Add(num);
        }
    }
}
