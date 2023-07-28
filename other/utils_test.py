# @author: code_king
# @date: 2023/7/28 9:54
from other.utils_callback import call_method


def print_test():
    return "test"


if __name__ == '__main__':
    # 在 file2.py 中调用 file1.py 中的 my_method 方法
    a = call_method(module_name="utils_test", method_name="print_test")
    print(f"a:{a}")
