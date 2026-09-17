class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        min_lens = [float('inf')] * n
        
        ans = float('inf')
        curr = 0
        l = 0
        min_len = float('inf')

        for r in range(n):
            curr += arr[r]
            
            while curr > target:
                curr -= arr[l]
                l += 1
                
            if curr == target:
                length = r - l + 1
                if l > 0 and min_lens[l - 1] != float('inf'):
                    ans = min(ans, length + min_lens[l - 1])
                    
                min_len = min(min_len, length)
                
            min_lens[r] = min_len

        return ans if ans != float('inf') else -1