# coding：utf-8
#author：jiguobin
# import tkinter as tk
#
# window = tk.Tk()
# window.title('my window')
# window.geometry('300x300')
#
# var=tk.StringVar()
# l=tk.Label(window,bg='yellow',width=20,text='empty')
# l.pack()
#
# def print_selection():
#     print('a')
#
# r1=tk.Radiobutton(window,text='Option A',
#                   variable=var,value='A',
#                   command=print_selection)
# r1.pack()
# r2=tk.Radiobutton(window,text='Option B',
#                   variable=var,value='B',
#                   command=print_selection)
# r2.pack()
# r3=tk.Radiobutton(window,text='Option C',
#                   variable=var,value='C',
#                   command=print_selection)
# r3.pack()
#
# window.mainloop()

from tkinter import *

#初始化Tk()
myWindow=Tk()
myWindow.title('Python GUI Learning')
myWindow.geometry('300x300')
v=IntVar()

#列表中存储的是元素是元组
ws_test=[('个人测试',0),('个体测试',1),('企业测试',2)]
ws_huidu=[('个人灰度',0),('个体灰度',1),('企业灰度',2)]
ws_online=[('个人生产',0),('个体生产',1),('企业生产',2)]

#定义单选按钮的响应函数
def callRB():
    for i in range(4):
        if (v.get()==i):
            root1 = Tk()
            if ws_test[i][0]=='客商':
                print(ws_test[i][0])
            if ws_test[i][0]=='网商':
                Label(root1,text='你的选择是'+ws_test[i][0]+'!',fg='red',width=20,height=6).pack()
                Button(root1,text='确定',width=3,height=1,command=root1.destroy).pack(side='bottom')
                print(ws_test[i][0])
            if ws_test[i][0]=='乐刷':
                Label(root1,text='你的选择是'+ws_test[i][0]+'!',fg='red',width=20,height=6).pack()
                Button(root1,text='确定',width=3,height=1,command=root1.destroy).pack(side='bottom')
                print(ws_test[i][0])


Label(myWindow,text='网商进件').pack(anchor=W)
#for循环创建单选框
for lan,num in ws_test:
    Radiobutton(myWindow, text=lan, value=num, command=callRB, variable=v).pack(anchor=N,side = LEFT)
for lan,num in ws_huidu:
    Radiobutton(myWindow, text=lan, value=num, command=callRB, variable=v).pack(fill=Y,side = BOTTOM)
# for lan,num in ws_online:
#     Radiobutton(myWindow, text=lan, value=num, command=callRB, variable=v).pack(fill=X,side = LEFT)


#进入消息循环R
myWindow.mainloop()










