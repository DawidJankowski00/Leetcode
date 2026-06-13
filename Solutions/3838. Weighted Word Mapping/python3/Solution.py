class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = ""
        ascii_a = ord('a')
        ascii_z = ord('z')
        for word in words:
            tmp = 0
            for v in word:
                tmp += weights[ord(v) - ascii_a]
            tmp %= 26
            result += chr(ascii_z - tmp)

        return result