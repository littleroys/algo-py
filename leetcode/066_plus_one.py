from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits


if __name__ == "__main__":
    s = Solution()
    result = s.plusOne([1, 2, 3, 4])
    print(result)
    result = s.plusOne([1, 2, 3, 9])
    print(result)
    result = s.plusOne([9, 9, 9, 9])
    print(result)
