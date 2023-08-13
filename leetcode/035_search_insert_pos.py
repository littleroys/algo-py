from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for idx, num in enumerate(nums):
            if target <= num:
                return idx
        return len(nums) 



if __name__ == "__main__":
    s = Solution()
    assert 2 == s.searchInsert([1, 3, 5, 6], 5)
    assert 1 == s.searchInsert([1, 3, 5, 6], 2)
    assert 4 == s.searchInsert([1, 3, 5, 6], 7)
