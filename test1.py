"""
 * Project name(项目名称)：Python位置参数和关键字参数
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/25 
 * Time(创建时间)： 19:55
 * Version(版本): 1.0
 * Description(描述)： Python位置参数
 位置参数，有时也称必备参数，指的是必须按照正确的顺序将实际参数传到函数中，换句话说，调用函数时传入实际参数的数量和位置都必须和定义函数时保持一致。
实参和形参数量必须一致
在调用函数，指定的实际参数的数量，必须和形式参数的数量一致（传多传少都不行），否则 Python 解释器会抛出 TypeError 异常，并提示缺少必要的位置参数。
 """


def f1(a, b):
    """
    数量演示
    :param a:
    :param b:
    :return:
    """
    return a + b


def f2(a, b):
    """
    位置演示
    :param a:
    :param b:
    :return:
    """
    return a + 3 * b


if __name__ == '__main__':
    # 位置不同时
    print(f2(4, 7))
    print(f2(7, 4))

    # 数量不同时
    print(f1(1, 2, 3))
