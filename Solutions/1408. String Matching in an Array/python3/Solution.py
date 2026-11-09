from collections import defaultdict
from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        st = " ".join(words)
        return [v for v in words if st.count(v) >=2]
