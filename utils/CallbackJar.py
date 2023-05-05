# coding=utf-8
# @Author:zcl01
# @Create_time:2023/5/5 14:46
# @File_name:CallbackJar
import time

import jpype


def test():
    _jar_base = './jar/chinatower_encrypt-1.0.jar'
    _jar_dirs = './jar'  # 依赖

    if not jpype.isJVMStarted():
        jpype.startJVM(jpype.getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % (_jar_base),
                       "-Djava.ext.dirs=%s" % (_jar_dirs)
                       )
    # jpype.addClassPath(_jar_base)
    SignOnClient = jpype.JClass("com.chinatower.encrypt.utils.Util")
    # self.record(SignOnClient)
    current_milli_time_str = str(int(round(time.time() * 1000)))
    result = SignOnClient.creterSM2Signature(current_milli_time_str, current_milli_time_str, "CHNTRLZYGL_RLYTHXT",
                                             "4f2d8a5f00f89a053e6f394cd9cb6c6b83bb5804044094ea2e87ba1d96d7b48d")
    # jpype.shutdownJVM()  # 关闭
    return str(result)


if __name__ == '__main__':
    result = test()
    print(result)

