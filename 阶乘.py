# 算一个数的阶乘
# 嵌套调用


a = int(input("请输入值(值要大于等于1)："))


def fruit(n):
    if n >= 1:
        return n * fruit(n - 1)
    else:
        return 1


# 调用然后输出
print(fruit(a))

