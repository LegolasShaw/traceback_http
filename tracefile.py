# -*- coding: utf-8 -*-

import sys
import traceback


def write_error_http(filename, err):
    # t, v, tb = sys.exc_info()
    # print(t)  # 异常类
    # print(v)  # 异常实例
    # print(tb)  # 异常代码跟踪
    #         print(traceback.print_tb(tb))
    # with open('err.txt', 'w') as f:
    #     traceback.print_tb(tb, file=f)

    print(filename)
    print(err.args[0])
    str1 = traceback.format_exc()

    print(str1)
