# coding=utf-8
# @Author:zcl01
# @Create_time:2023/4/6 20:01
# @File_name:JSUtils


def zip_code(code):
    """
    压缩js代码
    :param code:压缩前的js代码
    :return:
    """
    code = code.replace("\n", "").replace(" ", "").replace("\t", "")
    ret = f"\"change\"=\"{code}\""
    return ret


if __name__ == '__main__':
    code = """
    function(scope, model) {
	    dataService.callHcmOpenApi('private.get_user_info_from_MDM', {
            'name': FORM().data.name,
            'number': FORM().data.number,
            'identity_card': FORM().data.identity_card
        }).then(function(data) {
            if (data.number_check === true) {
                SCOPE.base_form.$setTip();
                FORM().data.NM = data.code
            } else {
                let tip = '查询到该人员（姓名' + FORM().data.name + '，身份证号' + FORM().data.identity_card +
                    '）在主数据平台中有编外人员账号，请确认是否转为正式人员。若是，请填写和主数据一致的编号';
                SCOPE.base_form.$setTip(tip)
            }
        })
    }
    """
    zipped_code = zip_code(code)
    print(zipped_code)
