# 给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 最后一个 单词的长度。
# 单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # words=s.split(" ")
        # for word in words[::-1]:
        #     if word!="":
        #         return len(word)
        return len(s.split()[-1])


# 输入：s = "Hello World"
# 输出：5
# 解释：最后一个单词是“World”，长度为5。
if __name__ == '__main__':
    s = "   fly me   to   the moon  "
    result = Solution().lengthOfLastWord(s)
    print(result)
