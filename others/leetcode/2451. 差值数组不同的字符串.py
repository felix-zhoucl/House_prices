# coding=utf-8
# @Author:zcl01
# @Create_time:2023/5/25 20:32
# @File_name:2451. 差值数组不同的字符串

# 给你一个字符串数组 words ，每一个字符串长度都相同，令所有字符串的长度都为 n 。
# 每个字符串 words[i] 可以被转化为一个长度为 n - 1 的 差值整数数组 difference[i] ，
# 其中对于 0 <= j <= n - 2 有 difference[i][j] = words[i][j+1] - words[i][j] 。
# 注意两个字母的差值定义为它们在字母表中 位置 之差，也就是说 'a' 的位置是 0 ，'b' 的位置是 1 ，'z' 的位置是 25 。
# 比方说，字符串 "acb" 的差值整数数组是 [2 - 0, 1 - 2] = [2, -1] 。
# words 中所有字符串 除了一个字符串以外 ，其他字符串的差值整数数组都相同。你需要找到那个不同的字符串。
#
# 请你返回 words中 差值整数数组 不同的字符串。
class Solution:
    def oddString(self, words: list[str]) -> str:
        a_word = None
        a_result = None
        b_word = None
        b_result = None
        for word in words:
            result = self.get_diff(word)
            print(f"result:{result}")
            if not a_word:
                a_word = word
                a_result = result
                continue
            elif not b_word:
                b_word = word
                b_result = result
                continue
            else:
                if result == a_result and result == b_result:
                    continue
                elif result == a_result:
                    return b_word
                elif result==b_result:
                    return a_word
                else:
                    return word

    @staticmethod
    def get_diff(word_str):
        """
        :param word_str:
        :return:
        """
        ret = []
        for index, x in enumerate(word_str):
            if index == 0:
                continue
            else:
                ret.append(ord(x) - ord(word_str[index - 1]))
        return ret


# 输入：words = ["adc","wzy","abc"]
# 输出："abc"
# 解释：
# - "adc" 的差值整数数组是 [3 - 0, 2 - 3] = [3, -1] 。
# - "wzy" 的差值整数数组是 [25 - 22, 24 - 25]= [3, -1] 。
# - "abc" 的差值整数数组是 [1 - 0, 2 - 1] = [1, 1] 。
# 不同的数组是 [1, 1]，所以返回对应的字符串，"abc"。
if __name__ == '__main__':
    words = ["aaa","bob","ccc","ddd"]
    result = Solution().oddString(words)
    print(f"result:{result}")
