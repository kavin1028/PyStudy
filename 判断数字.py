s = input('请输入文本：')
num = 0
for i in s:
    if i.isdigit():
        num += 1
print("一共有%d个数字" % num)