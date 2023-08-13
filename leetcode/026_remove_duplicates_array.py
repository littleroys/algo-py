from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = j = 0
        while j < len(nums):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i + 1


if __name__ == "__main__":
    l1 = [1, 1, 2]
    s = Solution()
    res = s.removeDuplicates(l1)
    print(res, ">>", l1)

    l2 = [0,0,1,1,1,2,2,3,3,4]
    s = Solution()
    res = s.removeDuplicates(l2)
    print(res, ">>", l2)
