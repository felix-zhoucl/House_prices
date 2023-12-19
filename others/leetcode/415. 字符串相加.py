# coding=utf-8
# @Author:zcl01
# @Create_time:2023/7/17 9:48
# @File_name:415. 字符串相加

# 题目
# 给定两个字符串形式的非负整数num1 和num2，计算它们的和并同样以字符串形式返回。
# 你不能使用任何內建的用于处理大整数的库（比如 BigInteger），也不能直接将输入的字符串转换为整数形式。
# 输入：num1 = "11", num2 = "123"
# 输出："134"

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        ans = []
        c = 0
        while i >= 0 or j >= 0 or c:
            a = 0 if i < 0 else int(num1[i])
            b = 0 if j < 0 else int(num2[j])
            c, v = divmod(a + b + c, 10)
            ans.append(str(v))
            i, j = i - 1, j - 1
        return "".join(ans[::-1])


if __name__ == '__main__':
    num1 = "1112"
    num2 = "2223"
    result = Solution().addStrings(num1, num2)
    print(f"result:{result}")
