'''
题目：画图，学用rectangle画方形。　　

程序分析：
rectangle(int left, int top, int right, int bottom)
参数说明：(left ，top )为矩形的左上坐标，(right,bottom)为矩形的右下坐标，两者可确定一个矩形的大小　
'''
from tkinter import *

root = Tk()
root.title('Canvas')
canvas = Canvas(root, width=400, height=400, bg='yellow')
x0 = 195
y0 = 195
x1 = 205
y1 = 205
for i in range(25):
    canvas.create_rectangle(x0, y0, x1, y1)
    x0 -= 5
    y0 -= 5
    x1 += 5
    y1 += 5
canvas.pack()
canvas.mainloop()
