class Solution:
    def processStr(self, s: str) -> str:
        result = ""

        for v in s:
            if v == "*":
                tmp = len(result)
                if tmp > 0:
                    result = result[0:tmp-1]
            elif v == "#":
                result = result + result
            elif v == "%":
                result = result[::-1]
            else:
                result += v
        return result