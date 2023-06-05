class GetChineseNumber(object):
    """
    动态私有OpenAPI
    使用方法
    """

    dictionary = {
        '0': '零',
        '1': '壹',
        '2': '贰',
        '3': '叁',
        '4': '肆',
        '5': '伍',
        '6': '陆',
        '7': '柒',
        '8': '捌',
        '9': '玖'
    }

    level1 = {
        1: '圆',
        2: '万',
        3: '亿',
        4: '兆'
    }

    level2 = {
        2: '拾',
        3: '佰',
        4: '仟'
    }

    level3 = {
        1: '角',
        2: '分'
    }

    def execute(self, number):
        number = str(number)
        result = self.convert(number)
        return result

    @staticmethod
    def process_integer(num_integer):
        pre = []
        length = len(num_integer)
        if length <= 4:
            pre.append(num_integer)
        else:
            extra = length % 4
            if extra != 0:
                pre.append(num_integer[0: extra])
                length = length - extra
                start, end = extra, 4 + extra
            else:
                start, end = 0, 4
            while length:
                pre.append(num_integer[start: end])
                start += 4
                end += 4
                length -= 4
        return pre

    def per_convert(self, num):
        length = len(num)
        flag = True

        # Special
        # deal with '0000'
        if num == '0000':
            return ''
        # deal with '1000'
        if num[1:] == '000':
            result = self.dictionary[num[0]] + self.level2[4]
            return result

        # Normal
        res, p = '', length
        for i in range(0, length):
            # deal with prefix is '0'
            if (res == '' or res == self.dictionary[num[i]]) and num[i] == '0':
                # only one '0'
                if flag:
                    res += self.dictionary[num[i]]
                    flag = False
                p -= 1
                continue
            # deal with '1001'
            if i + 1 < length and num[i + 1] == '0' and num[i] == '0':
                p -= 1
                continue
            # deal with '1010' '1110'
            if i == length - 1 and num[i] == '0':
                continue
            res += self.dictionary[num[i]]
            if p > 1 and num[i] != '0':
                res += self.level2[p]
            p -= 1
        return res

    def convert_integer(self, ans_int):
        res = ''
        p = len(ans_int)
        for i in ans_int:
            per_res = self.per_convert(i)
            res += per_res
            if p > 0 and per_res != '':
                res += self.level1[p]
            p -= 1
        return res

    def convert_float(self, num_float):
        res = ''
        for i in range(0, len(num_float)):
            res += self.dictionary[num_float[i]]
            if (i + 1) <= 2:
                res += self.level3[i + 1]
        return res

    def convert(self, number):

        res = ''
        if '.' in number:
            num_split = number.split('.')
            num_integer = num_split[0]
            num_float = num_split[1]
            ans_int = self.process_integer(num_integer)
            # print(ans_int)
            # Convert integer
            res += self.convert_integer(ans_int)
            # Convert float
            res += self.convert_float(num_float)
        else:
            ans_int = self.process_integer(number)
            res += self.convert_integer(ans_int)
        return res
