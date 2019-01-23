# 九九乘法表
"""
for i in range(1, 10):
    for m in range(1, i):
        print(end="       ")
    for j in range(i, 10):
        k = i * j
        print('%d*%d=%2d' % (i, j, k), end=' ')
    print()

"""
for i in range(1, 10):
    s = ""
    for j in range(1, i+1):
        # s += "{1}*{0}={2} ".format(i, j, i*j)
        # print("{1}*{0}={2} ".format(i, j, i*j), end='')
        s += "%d*%d=%-3d" % (j, i, j*i)
    print(s)
