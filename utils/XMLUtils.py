# coding=utf-8
# @Author:zcl01
# @Create_time:2023/6/16 16:26
# @File_name:XMLUtils

import xmltodict

xml_str = '<?xml version=\"1.0\" encoding=\"UTF-8\"?>' \
          '<USERMODIFYRSP>\\n' \
              '<HEAD>\\n' \
                  '<CODE/>\\n' \
                      '<SERVICEID>CHNTRLZYGL_RLYTHXT</SERVICEID>\\n' \
                      '<SID/>\\n' \
                          '<TIMESTAMP>1686896520549</TIMESTAMP>\\n' \
                             '</HEAD>\\n' \
                                '<BODY>\\n' \
                                  '<ERRDESC>601<ERRDESC/>\\n' \
                                  '<LOGINNO>null</LOGINNO>\\n' \
                                  '<MODIFYMODE>add</MODIFYMODE>\\n' \
                                  '<RSP>1</RSP>\\n' \
                                  '<USERID>null</USERID>\\n' \
                                '</BODY>\\n' \
          '</USERMODIFYRSP>\\n'
res_dict = xmltodict.parse(xml_str)
print(res_dict)
