class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        result = 0
        tmp = [False] * 1000
        l = len(digits)
        for i in range(l):
            if digits[i] == 0:
                continue
            for j in range(l):
                if i == j:
                    continue
                for k in range(l):
                    if j == k or i == k:
                        continue
                    if digits[k] % 2 == 0:
                        x = digits[i] * 100 + digits[j] * 10 + digits[k]
                        if not tmp[x]:
                            tmp[x] = True
                            result += 1
        return result