from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]]
        for _ in range(rowIndex):
            temp = [0] + res[-1] + [0]
            new_row = []
            for i in range(len(temp) - 1):
                new_row.append(temp[i] + temp[i +1])
            res.append(new_row)
        return res[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.getRow(0))
    print(s.getRow(1))
    print(s.getRow(2))
    print(s.getRow(3))