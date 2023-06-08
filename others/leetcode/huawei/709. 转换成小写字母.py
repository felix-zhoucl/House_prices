# 给你一个字符串 s ，将该字符串中的大写字母转换成相同的小写字母，返回新的字符串。


class Solution:
    def toLowerCase(self, s: str) -> str:
        # ret=""
        # for i in s:
        #     i = i.lower()
        #     ret+=i
        # return ret
        return "".join(chr(asc | 32) if 65 <= (asc := ord(ch)) <= 90 else ch for ch in s)


if __name__ == '__main__':
    s = "helloWorOld"
    result = Solution().toLowerCase(s)
    print(result)
