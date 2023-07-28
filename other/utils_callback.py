# @author: code_king
# @date: 2023/7/28 9:54


import importlib


def call_method(module_name, method_name):
    module = importlib.import_module(module_name)
    method = getattr(module, method_name)
    return method()
    # print(f"调用的内容 {method()}")
