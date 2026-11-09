import sys
def main():
    sol = Solution()
    print(sol.isPalindrome(121))

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x)[::-1] == str(x):
            return True
        else:
            return False

if __name__ == '__main__':
    sys.exit(main())