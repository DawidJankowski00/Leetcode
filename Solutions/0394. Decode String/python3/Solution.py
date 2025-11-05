class Solution:
    def decodeString(self, s: str) -> str:
        k = 0
        n = len(s)
        def createPart():
            nonlocal k, n
            result = ""
            while k < n and s[k] != ']':
                if s[k].isdigit():
                    dig_start = k
                    while s[k] != "[":
                        k += 1
                    tmp = s[dig_start:k]
                    k += 1
                    tmp2 = createPart()
                    for _ in range(int(tmp)):
                        result += tmp2
                else:
                    result += s[k]
                    k += 1
            k += 1
            return result
        return createPart()