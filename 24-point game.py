# 两个数运算

def cp(m, op, n):
    """
    if m == 99999999 or n == 999999999:
        return 9999999999
    else:
        pass
        用try（异常）更简单
    """
    if '+' == op:
        return m + n
    elif '-' == op:
        return m - n
    elif '*' == op:
        return m * n
    else:
        # if 0 != c:
            return m / n
        # else:
        # return 99999999


a = int(input("请输入a的数值:"))
b = int(input("请输入b的数值:"))
c = int(input("请输入c的数值:"))
d = int(input('请输入d的数值:'))

list1 = [a, b, c, d]
op = ["+", "-", "*", "/"]

for e in list1:
    list2 = list1.copy()  # 引用
    list2.remove(e)  # 删除列表中第一个元素
    for f in list2:
        list3 = list2.copy()
        list3.remove(f)
        for g in list3:
            list4 = list3.copy()
            list4.remove(g)
            for h in list4:

                for x in op:
                    for y in op:
                        for z in op:

                            try:  # 标记错误
                                # (a+b)+(c+d)
                                if 24 == cp(cp(e, x, f), y, cp(g, z, h)):
                                    print("算法1：")
                                    print("(%d%s%d)%s(%d%s%d) = 24" % (e, x, f, y, g, z, h,))
                            except ZeroDivisionError:
                                pass

                            try:
                                # ((a+b)+c)+d
                                if 24 == cp(cp(cp(e, x, f), y, g), z, h):
                                    print("算法2：")
                                    print("((%d%s%d)%s%d)%s%d = 24" % (e, x, f, y, g, z, h,))
                            except ZeroDivisionError:
                                pass

                            try:
                                # (a+(b+c)+d
                                if 24 == cp(cp(e, x, cp(f, y, g)), z, h):
                                    print("算法3：")
                                    print("(%d%s(%d%s%d)%s%d) = 24" % (e, x, f, y, g, z, h,))
                            except ZeroDivisionError:
                                pass

                            try:
                                # a+((b+c)+d)
                                if 24 == cp(e, x, cp(cp(f, y, g, ), z, h)):
                                    print("算法4：")
                                    print("%d%s(%d%s%d)%s%d)) = 24" % (e, x, f, y, g, z, h,))
                            except ZeroDivisionError:
                                    pass

                            try:
                                # a+(b+(c+d))
                                if 24 == cp(e, x, cp(f, y, cp(g, z, h))):
                                    print("算法5：")
                                    print("%d%s(%d%s(%d%s%d)) = 24" % (e, x, f, y, g, z, h,))
                            except ZeroDivisionError:
                                pass  # 处理异常
