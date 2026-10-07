class Solution:
    def reverseString(self, s: list[str]) -> None:
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

if __name__ == "__main__":
    sol = Solution()
    test_s = ["h", "e", "l", "l", "o"]
    sol.reverseString(test_s)
    print(test_s)  # 输出 ['o', 'l', 'l', 'e', 'h']