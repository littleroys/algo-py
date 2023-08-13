from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]


if __name__ == "__main__":
    l1 = [1, 2, 3, 4, 1, 1, 1]
    s = Solution()
    print(s.majorityElement(l1))
    print(1534236469 >= 2 **31)


