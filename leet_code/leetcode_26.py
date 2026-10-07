class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
                
        return slow + 1  # 返回长度

if __name__ == "__main__":
    sol = Solution()
    test_nums = [0, 0, 1, 1, 2]
    k = sol.removeDuplicates(test_nums)
    print(f"长度: {k}, 数组前{k}项: {test_nums[:k]}")