class Solution:
    def processStr(self, s: str, k: int) -> str:
        target_length = self._calculate_final_length(s)

        if k >= target_length:
            return '.'

        return self._find_char_at_index(s, k, target_length)


    def _calculate_final_length(self, s: str) -> int:
        target_length = 0
        for char in s:
            if char == '*':
                target_length = max(target_length - 1, 0)
            elif char == '#':
                target_length *= 2
            elif char != '%':
                target_length += 1
        return target_length


    def _find_char_at_index(self, s: str, k: int, target_length: int) -> str:
        str_length = len(s)
        
        for i in range(str_length - 1, -1, -1):
            char = s[i]
            if char == '*':
                target_length += 1
            elif char == '#':
                half_length = target_length // 2
                if k >= half_length:
                    k -= half_length
                target_length //= 2
            elif char == '%':
                k = target_length - 1 - k
            else:
                if target_length == k + 1:
                    return char
                target_length -= 1
                
        return '.'