# 给你一个下标从 0 开始、大小为 n x n 的整数矩阵 grid ，返回满足 Ri 行和 Cj 列相等的行列对 (Ri, Cj) 的数目。
# 如果行和列以相同的顺序包含相同的元素（即相等的数组），则认为二者是相等的。

class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        column = []
        for index, number in enumerate(grid[0]):
            info = []
            for group in grid:
                info.append(group[index])
            column.append(info)
        print(f"column:{column}")


# 输入：grid = [[3,2,1],[1,7,6],[2,7,7]]
# 输出：1
# 解释：存在一对相等行列对：
# - (第 2 行，第 1 列)：[2,7,7]

if __name__ == '__main__':
    grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
    result = Solution().equalPairs(grid)
    print(result)
