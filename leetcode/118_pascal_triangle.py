from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for _ in range(numRows - 1):
            last_row = res[-1]
            i = -1
            next_row = []
            for j in range(len(last_row)):
                if i == -1:
                    next_row.append(last_row[j])
                else:
                    next_row.append(last_row[j] + last_row[i])
                i = j
                j += 1
            next_row.append(1)
            res.append(next_row)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.generate(1))
    print(s.generate(2))
    print(s.generate(3))
