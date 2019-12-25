"""
验证输入用户名和QQ号是否有效并给出对应的提示信息

要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
"""
import re


def main():
    str1 = '999'
    # # 匹配正整数
    # r = re.match(r'^[1-9]\d*$', str1)
    # 匹配三个数字
    r = re.match(r'\d{3}$', str1)
    if r:
        print('true')
    else:
        print('false')


if __name__ == '__main__':
    main()
