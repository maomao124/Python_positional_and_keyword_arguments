"""
 * Project name(项目名称)：Python位置参数和关键字参数
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/25 
 * Time(创建时间)： 20:00
 * Version(版本): 1.0
 * Description(描述)： Python函数关键字参数
 关键字参数是指使用形式参数的名字来确定输入的参数值。通过此方式指定函数实参时，不再需要与形参的位置完全一致，只要将参数名写正确即可。
 """


def f2(a, b):
    """
    位置演示
    :param a:
    :param b:
    :return:
    """
    return a + 3 * b


if __name__ == '__main__':
    print(f2(6, 7))
    # print(f2(7, 6))
    # 关键字参数
    print(f2(a=6, b=7))
    print(f2(6, b=7))
    # 不允许
    # print(f2(a=6, 7))
