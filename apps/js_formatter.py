# coding=utf-8
# @Author:zcl01
# @Create_time:2023/4/13 11:10
# @File_name:js_formatter
import utils.JSUtils as formatter
js_str = """
"func": "=function(){var filter_year_month=SCOPE.filter_year_month;var items=ITEMS();dataService.callHcmOpenApi('private.submit_result_confirm',{'year_month':filter_year_month,'data':items}).then(function(data){SCOPE.show_warning(data)})}",
"""


if __name__ == '__main__':
    ret = formatter.unzip_code(js_str)
    print(ret)