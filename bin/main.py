# coding：utf-8
# author：jiguobin
from case.Ws import WsPage
from case.Ks import KsPage
from tkinter import *
from tkinter import ttk
#
#初始化Tk()
myWindow=Tk()
myWindow.title('mc自动化')
myWindow.geometry('300x400')
v=IntVar()
case_sheet= StringVar()
case_name = StringVar()
case_row=StringVar()


#列表中存储的是元素是元组
# ws_test=[('个人测试',0,3),('个体测试',1,0),('企业测试',2,0),
#          ('个人灰度',3,0),('个体灰度',4,0),('企业灰度',5,0),
#          ('个人生产',6,0),('个体生产',7,0),('企业生产',8,0)]
ws_test=[('网商个人','个人测试',0,2)]



#定义单选按钮的响应函数

def callRB():
	for i in range(len(ws_test)):
		if (v.get()==i):
			root1 = Tk()
			if ws_test[i][0]=='网商个人':
				Button(root1, text='进件', width=3, height=1, command=lambda:b2(root1,i)).pack(side='bottom')
			if ws_test[i][0]=='网商个体':
				Button(root1, text='进件', width=3, height=1, command=lambda: b3(root1,i)).pack(side='bottom')
			if ws_test[i][0]=='网商企业':
				Button(root1, text='进件', width=3, height=1, command=lambda: b4(root1, i)).pack(side='bottom')
			if ws_test[i][0]=='客商个人':
				Button(root1, text='进件', width=3, height=1, command=lambda: b5(root1, i)).pack(side='bottom')
			if ws_test[i][0]=='客商企业':
				Button(root1, text='进件', width=3, height=1, command=lambda: b6(root1, i)).pack(side='bottom')
			if ws_test[i][0]=='乐刷个人':
				Button(root1, text='进件', width=3, height=1, command=lambda: b7(root1, i)).pack(side='bottom')
			if ws_test[i][0]=='乐刷企业':
				Button(root1, text='进件', width=3, height=1, command=lambda: b8(root1, i)).pack(side='bottom')
			Label(root1, text='你的选择是' + ws_test[i][1] + '!', 
fg='red', width=20, height=6).pack()
#进件
def b2(root1,i):
	w = WsPage('网商个人', int(ws_test[i][3]))
	# w.main()
	root1.destroy()
def b3(root1,i):
	w = WsPage('网商个体', int(ws_test[i][3]))
	root1.destroy()
def b4(root1,i):
	w = WsPage('网商企业', int(ws_test[i][3]))
	root1.destroy()
def b5(root1,i):
	k = KsPage('客商个人', int(ws_test[i][3]))
	root1.destroy()
def b6(root1,i):
	k = KsPage('客商企业', int(ws_test[i][3]))
	root1.destroy()
def b7(root1,i):
	k = KsPage('乐刷个人', int(ws_test[i][3]))
	root1.destroy()
def b8(root1,i):
	k = KsPage('乐刷企业', int(ws_test[i][3]))
	root1.destroy()




#添加用例
def b1():
	print (case_sheet.get())
	ws_test.append((case_sheet.get(),case_name.get(),len(ws_test),case_row.get
()))
	# file = open('data.txt', 'w')
	# file.write(str(ws_test));
	# file.close()
	print (ws_test)
	s = 0
	m = 20
	for sheet,lan, num, row in ws_test:
		if s == 300:
			m = m + 30
			s = 0
		Radiobutton(myWindow, text=lan, value=num, command=callRB, 
variable=v).place(x=s, y=m)
		s = s + 100
		print



#for循环创建单选框
s=0
m=20
for sheet,lan,num,row in ws_test:
    if s==240:
        m=m+20
        s=0
    Radiobutton(myWindow, text=lan, value=num, command=callRB, variable=v).place(x=s, 
y=m)
    s = s + 80



Label(myWindow, text='sheet').place(x=40,y=270)
# Entry(myWindow, textvariable=case_sheet).place(x=100,y=270)
# 创建一个下拉列表

numberChosen =ttk.Combobox(myWindow, width=12, textvariable=case_sheet)
numberChosen['values'] = ('网商个人', '网商个体', '网商企业', '客商个人', '客商企业','乐刷个人','乐刷企业','新增商户','新增门店')  # 设置下拉列表的值
numberChosen.place(x=100,y=270) # 设置其在界面中出现的位置  column代表列   row 代表行
numberChosen.current(0)  # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值

Label(myWindow, text='用例名称').place(x=40,y=300)
Entry(myWindow, textvariable=case_name).place(x=100,y=300)
Label(myWindow, text='行      数').place(x=40,y=330)
Entry(myWindow, textvariable=case_row).place(x=100,y=330)


Button(myWindow, text='确定', width=3, height=1, command=b1).pack(side='bottom')



# Radiobutton(myWindow, text=lan, value=num, command=callRB, variable=v).pack()
# Radiobutton(myWindow, text=ws_test[0][0], value=0, command=callRB, variable=v).place(x=20,y=20)
# Radiobutton(myWindow, text=ws_test[1][0], value=1, command=callRB, variable=v).place(x=100,y=20)
# Radiobutton(myWindow, text=ws_test[2][0], value=2, command=callRB, variable=v).place(x=180,y=20)



#进入消息循环R
myWindow.mainloop()

















