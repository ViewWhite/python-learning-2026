# 暴力解法
class SolutionBruteForce:
    def twoSum(self, nums, tg):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == tg:
                    return [i, j]
        return []

# 哈希表解法（最优解）
class Solution:
    def twoSum(self, nums, tg):
        hashmap = {}
        for i, num in enumerate(nums):
            need = tg - num
            if need in hashmap:
                return [hashmap[need], i]
            hashmap[num] = i
        return []

if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))  # 输出 [0, 1]