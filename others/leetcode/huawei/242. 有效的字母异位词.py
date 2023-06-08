# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
# 注意：若s 和 t中每个字符出现的次数都相同，则称s 和 t互为字母异位词。


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # count_dict = {}
        # for alpha in s:
        #     if s not in count_dict:
        #         count_dict[alpha] = s.count(alpha)
        # for alpha in t:
        #     if t.count(alpha) != count_dict.get(alpha):
        #         return False
        # return True
        return sorted(s) == sorted(t)


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    result = Solution().isAnagram(s, t)
    print(result)

# 输入: s = "anagram", t = "nagaram"
# 输出: true
