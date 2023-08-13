from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i


if __name__ == "__main__":
    l1 = [0, 1, 2, 2, 2, 3, 4]
    s = Solution()
    res = s.removeElement(l1, 2)
    print(res, l1)
