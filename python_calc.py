#-*-coding:utf-8-*-
from tkinter import *
#创建窗口
window = Tk()
#设置窗口标题
window.title("this is a test window")
#设置窗口大小
window.geometry("480x400")
#设置窗口的width不可变，height可变
window.resizable(width=False,height=True)
#将窗口进行无限循环
window.mainloop()