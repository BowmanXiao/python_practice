'''
题目：
猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个；第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了，求第一天共摘了多少？

程序分析：采取逆向思维的方法，从后往前推断。
'''


# 求第一天共摘了多少桃子，即求第一天吃前的桃子总数。由题干条件可知，第10天吃前桃子总数为1。
# 根据题干信息，第一天吃前桃子总数等于第二天吃前桃子总数加一再乘以二。。。
# 第九天吃前桃子总数等于第十天吃前桃子总数加一再乘以二，因此可采用递归函数倒序求解。
def peach(n):
    if n == 10:
        return 1
    else:
        return (peach(n + 1) + 1) * 2


print('第一天共摘了{}个桃子。'.format(peach(1)))


# 第一天吃桃数=第一天总数-第二天总数
def eat(n):
    if n > 0 and n < 10:
        return peach(n) - peach(n + 1)
    else:
        return 1

eat_dict = {}
for i in range(1, 11):
    eat_dict[i] = eat(i)
    print('第{}天吃了{}个桃子。'.format(i, eat_dict[i]))
print(eat_dict)

# eat_list = []
# for i in range(1, 11):
#     eat_list.append(eat(i))
#     print('第{}天吃了{}个桃子。'.format(i, eat(i))
# print(eat_list)
