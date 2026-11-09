import sys
def main():
    sol = Solution()
    print(sol.romanToInt("MCMXCIV"))

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        extravalues = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        result = 0
        i = 0
        while i+1 < len(s):
            if s[i] + s[i+1] in extravalues:
                result += extravalues[s[i] + s[i+1]]
                i += 2
            else:
                result += values[s[i]]
                i+=1
        if i == len(s)-1:
            result += values[s[i]]
        return result

        

if __name__ == '__main__':
    sys.exit(main())