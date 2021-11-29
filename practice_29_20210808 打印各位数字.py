'''
给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

程序分析：学会分解出每一位数。
'''

# 方法一 取整、取余
x = int(input("请输入一个数：\n"))
a = x // 10000
b = x % 10000 // 1000
c = x % 1000 // 100
d = x % 100 // 10
e = x % 10
if a!=0:
    print('5位数：', e, d, c, b, a)
elif b!=0:
    print('4位数：', e, d, c, b)
elif c!=0:
    print('3位数：', e, d, c)
elif d!=0:
    print('2位数：', e, d)
else:
    print('1位数：', e)

# 方法二 字符串转列表，切片逆序输出
x= input("请输入一个数：\n")
listx=list(x)
print(f"{len(listx)}位数：{listx[::-1]}")
