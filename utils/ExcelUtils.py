# coding=utf-8
# @Author:zcl01
# @Create_time:2023/4/3 9:54
# @File_name:ExcelUtils
import xlsxwriter

workbook = xlsxwriter.Workbook("test.xslx")  # 创建excel文件

worksheet1 = workbook.add_worksheet('操作日志')  # 括号内为工作表表名

bold = workbook.add_format({

    'bold': True,  # 字体加粗

    'border': 1,  # 单元格边框宽度

    'align': 'left',  # 水平对齐方式

    'valign': 'vcenter',  # 垂直对齐方式

    'fg_color': '#F4B084',  # 单元格背景颜色

    'text_wrap': True,  # 是否自动换行

})

# row:行索引， col：列索引， data:要写入的数据, bold:单元格的样式
# 索引下标从0开始
worksheet1.write(1, 3, "data_1", bold)

# A1:从A1单元格开始插入数据，按行插入， data:要写入的数据（格式为一个列表), bold:单元格的样式
worksheet1.write_row("A1", "data_2", bold)

# 　A1:从A1单元格开始插入数据，按列插入， data:要写入的数据（格式为一个列表), bold:单元格的样式
worksheet1.write_column("A1", "data_3", bold)

# 　第一个参数是插入的起始单元格，第二个参数是图片你文件的绝对路径

# worksheet1.insert_image('A1', 'f:\\1.jpg')
#
# worksheet1.merge_range()  # 合并单元格

workbook.worksheets()  # 获得当前excel文件的所有工作表

workbook.close()  # 关闭excel文件
