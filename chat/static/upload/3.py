import tkinter as tk
from tkinter import *
import tkinter.messagebox
from tkinter import scrolledtext
import socket
import time
from PIL import ImageTk, Image
import sys


client = socket.socket()#创建实例
ip_port = ("192.168.43.15",8888)#绑定ip和port
ip_port2 = ("103.46.128.41",48237)
ip_port3 =('111.231.116.244',47871)
client.connect(ip_port3)#连接主机

#登录注册主页面
window = tk.Tk()
window.title('MYchat')
window.geometry('450x300')
window.resizable(0,0)


#登录函数
def login():#登录后进入主页面
	
	def main_window():
		window2 = tk.Tk()
		window2.geometry('540x380')
		window2.resizable(0,0)
					
		def btn_new4():#获取信息
			
			try:
				onename1 = lb.get(lb.curselection())
				onename = onename1.replace("联系人------","",1)
			except BaseException:
				tk.messagebox.showwarning(message='用户都不选你想获取什么？？')	
			else:
				if onename1 == "----------------本地联系人----------------":
					tk.messagebox.showwarning(message='这个可不是联系人')
				else:
					window6 = Toplevel(window2)
					window6.geometry('300x400')
					window6.resizable(0,0)
					
					canvas2 = tk.Canvas(window6, width=300,height=400,bd=0, highlightthickness=0)
					canvas2.create_image(80, 200,image=photo)
					canvas2.place(x=0,y=0)
					
					gi = "yes"
					gp = "ok"
					selection = "huoqu"
					client.send(selection.encode())
					date = client.recv(1024)
					if date == b"yes":
						client.send(onename.encode())
					
					Sname = client.recv(1024).decode()
					client.send(gp.encode())
					Sid = client.recv(1024).decode()
					client.send(gp.encode())
					School = client.recv(1024).decode()
					client.send(gp.encode())
					Class = client.recv(1024).decode()
					client.send(gp.encode())
					Major = client.recv(1024).decode()
					client.send(gp.encode())
					date = client.recv(1024)
								
								
					lb1=tk.Label(window6, text='姓名: '+Sname).place(x=50, y= 100)
					lb2=tk.Label(window6, text='学校：'+School).place(x=50, y= 130)
					lb3=tk.Label(window6, text='专业：'+Major).place(x=50, y= 160)
					lb4=tk.Label(window6, text='班级：'+Class).place(x=50, y= 190)
					lb5=tk.Label(window6, text='学号：'+Sid).place(x=50, y= 220)
					
					canvas2.create_window(87,100,width=100,window=lb1)
					canvas2.create_window(87,130,width=100,window=lb2)
					canvas2.create_window(87,160,width=100,window=lb3)
					canvas2.create_window(87,190,width=100,window=lb4)
					canvas2.create_window(87,220,width=100,window=lb5)
			
		def btn_new3():#关于函数
			window6 = tk.Toplevel(window2)
			window6.geometry('300x400')
			window6.resizable(0,0)
			
			canvas1 = tk.Canvas(window6, width=300,height=400,bd=0, highlightthickness=0)
			canvas1.create_image(80, 200,image=photo)
			canvas1.place(x=0,y=0)
			
			gi = "yes"
			gp = "ok"
			selection = "guanyu"
			client.send(selection.encode())
			date = client.recv(1024)
			if date == b"yes":
				client.send(name.encode())
			
			Sname = client.recv(1024).decode()
			client.send(gp.encode())
			Sid = client.recv(1024).decode()
			client.send(gp.encode())
			School = client.recv(1024).decode()
			client.send(gp.encode())
			Class = client.recv(1024).decode()
			client.send(gp.encode())
			Major = client.recv(1024).decode()
			client.send(gp.encode())
			date = client.recv(1024)
						
						
			la1=tk.Label(window6, text='姓名: '+Sname)
			la2=tk.Label(window6, text='学校：'+School)
			la3=tk.Label(window6, text='专业：'+Major)
			la4=tk.Label(window6, text='班级：'+Class)
			la5=tk.Label(window6, text='学号：'+Sid)
			

			canvas1.create_window(87,100,width=100,window=la1)
			canvas1.create_window(87,130,width=100,window=la2)
			canvas1.create_window(87,160,width=100,window=la3)
			canvas1.create_window(87,190,width=100,window=la4)
			canvas1.create_window(87,220,width=100,window=la5)

			
		def btn_newx():#显示全部用户函数
			gi = "yes"
			gp = "ok"
			selection = "allxianshi"
			client.send(selection.encode())
			lb.delete(0,END)
			lb.insert(END,"----------------本地联系人----------------")
			date = client.recv(1024)
			if date == b"yes":
				client.send(gi.encode())
				while True:
					date = client.recv(1024)
					if date == b"Nomore":
						client.send(gp.encode())
						break
					else:
						nowname = date.decode()
						lb.insert(END,"联系人------"+nowname)
						client.send(gi.encode())
			l = lb.after(10000,btn_newx)
					
		def btn_new2(): #进入聊天室		
			def main():
				try:
					onename1 = lb.get(lb.curselection())
					onename = onename1.replace("联系人------","",1)
				except BaseException:
					tk.messagebox.showwarning(message='用户都不选你想获取什么？？')	
				else:
					if onename1 == "----------------本地联系人----------------":
						tk.messagebox.showwarning(message='这个可不是联系人')
					else:
						def getmessage():#获取聊天记录
							gi = "yes"
							gp = "ok"
							gy = 'no'
							selection = "getmessage"
							Hisname = onename
							
							if Hisname == '':
								txtMsgList.delete('0.0',END)
								txtMsgList.insert(END, '               welcome!!!'+'\n'+'            请选择联系人，进行聊天!', 'red')   #插入到tag位置
								
							else:
								txtMsgList.delete('0.0',END)
								client.send(selection.encode())
								date = client.recv(1024)
								
								if date == b'yes':
									client.send(name.encode())
									date = client.recv(1024)
									client.send(Hisname.encode())
									while True:
										date = client.recv(1024)
										if date == b'noallmore':
											client.send(gp.encode())
											break
										else:
											if date == b'ok':
												client.send(gp.encode())
												date = client.recv(1024)
												msg = date.decode()
												client.send(gp.encode())
												
												txtMsgList.insert(END, Hisname+':'+msg, 'red')   #插入到tag位置
											else:
												client.send(gp.encode())
												date = client.recv(1024)
												msg = date.decode()
												client.send(gp.encode())
												txtMsgList.insert(END, msg, 'greencolor')   #插入到tag位置
												
							txtMsgList.after(4000,getmessage)
											
										
						def btn_newy():#显示用户函数
							gi = "yes"
							gp = "ok"
							selection = "xianshi"
							client.send(selection.encode())
							listLianxi.delete(0,END)
							date = client.recv(1024)
							if date == b"yes":
								client.send(gi.encode())
								while True:
									date = client.recv(1024)
									if date == b"Nomore":
										client.send(gp.encode())
										break
									else:
										nowname = date.decode()
										listLianxi.insert(END,"在线联系人------"+nowname)
										client.send(gi.encode())
							
						def sendMsg():                  #发送消息
							strMsg = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + '\n ' +txtMsg.get('0.0', END)
							hisname = onename
							
							if txtMsg.get('0.0',END)[:-1] == '':
								tk.messagebox.showinfo(message='没话说，你发什么消息？!')
							elif hisname == '':
								tk.messagebox.showinfo(message='选择联系人!')
							else:
							
								gi= 'yes'
								gj= 'no'
								selection = 'fasong'
								
								client.send(selection.encode())
								date = client.recv(1024)
								
								if date == b'yes':
									client.send(name.encode())
									date = client.recv(1024)
									client.send(hisname.encode())
									date = client.recv(1024)
									client.send(strMsg.encode())
									date = client.recv(1024)
									if date == b'ok':
										txtMsg.delete('0.0', END)
									else :
										tk.messagebox.showinfo(message='send messages woring!')
									
						def showtime():        #时间模块，开启之后会影响运行速度
							
							timeText.delete(1.0,END)
							timeText2.delete(1.0,END)
							Time1 = time.strftime("   %H:%M:%S",time.localtime()) + '\n '
							Time2 = time.strftime("  %Y/%m/%d",time.localtime()) + '\n '
							Time3 = time.strftime("   %A",time.localtime()) + '\n '
								
							timeText.insert(END, Time1)
							timeText2.insert(END, Time2)
							timeText2.insert(END, Time3)
								
							time.sleep(1)
							timeText.update()
							
							timeText.after(60000,showtime)
							timeText2.after(60000,showtime)
							
							
						def cancelMsg():                #取消消息
							txtMsg.delete('0.0', END)
							
						def exitMsg():                  #退出聊天界面
							t.destroy()
							main_window()
							
						def sendMsgEvent(event):        #发送消息事件
							if event.keysym == "Return":  #按回车键可发送
								sendMsg()
								
								
						def red():                      #Canvas背景色控制
							imgCanvas.config(bg='red')
						def green():
							imgCanvas.config(bg='green')
						def blue():
							imgCanvas.config(bg='blue')
						def color1():
							names = ['red', 'green', 'blue','yellow','white','SlateGray','SpringGreen','LightSteelBlue','Cyan','BlueViolet','GhostWhite']
							for i in names:
								imgCanvas.config(bg=i)
								time.sleep(0.4)
								imgCanvas.update()
								
						def Oval():                     #Canvas绘制几何图案
							imgCanvas.create_oval(110, 20, 170, 120)
						def Polygon():
							imgCanvas.create_polygon(20, 20, 110, 50,100,110,40,120)
							
						def fontSize(ev=None):          #字体缩放
							timeText2.config(font='Helvetica -%d bold' % sizeScale.get())
							sizeLabel.config(text='字号：%d'% sizeScale.get())
						
						def txtlist():                  #字典实现--书名与内容的对应
							book={'NO.3 《平凡的世界》  路遥':'1.一个平平常常的日子，细蒙蒙的雨丝夹着一星半点的雪花，正纷纷淋淋的向大地飘洒着，时令已快到惊蛰，雪当然再不会存留，往往还没等落地，就消失的无踪无影了，黄土高原严寒而漫长的冬天看来就要过去，但那真正温暖的春天还远远没有到来。\n2、这时候，他也体验到了类似孙少平的那种感觉：只有繁重的体力劳动才使精神上的痛苦变为某种麻木，以致思维局限在机械性活动中。\n3、哭，笑，都是因为欢乐，哭的人知道而笑的人不知道，这欢乐是多少痛苦所换来的。',
								  'NO.2 《看见》  柴静':'1.写本身也是一种发现自己的过程，你不写永远都知道自己身上发生了什么。\n2.保持对不同论述的警惕，才能保持自己的独立性。\n3.灵魂变得沉重，是因为爱，因为所爱的东西，眼睁睁在失去，却无能为力。\n4.我可能做不到更好了，但还是要像朱光潜说的那样，此时，此地，此身，此时我能做的事情绝不推诿到下一时刻，此地我能做的事情绝不换另一种境地再去做，此身我能做的事绝不妄想与他人来替代。\n5.如果带着强烈的预设和反感，你就没有办法真的认识这个人。',
								  'NO.1 《超级聊天室》  顺':'1.欢迎来到超级聊天室！！！！\n2.此软件用于C/S的临时聊天软件，采用udp协议。S\n3.C/S分布式模式，是计算机用语。C是指Client，S是指Server。C/S模式就是指客户端/服务器模式。是计算机软件协同工作的一种模式。'}
								  
							txtText.delete(0.0,END)
							txtText.insert(END,book[txtSpinbox.get()])
							 

							
						window2.destroy()
						t = tk.Tk()
						t.title(name)
						t.resizable(0,0)
						
						###  创建frame容器 ###
						
						frmA1 = Frame(width=180,height=30)
						frmA2 = Frame(width=180,height=290)
						frmA3 = Frame(width=180,height=140)
						frmA4 = Frame(width=180,height=30)
						
						frmB1 = Frame(width=350, height=320)
						frmB2 = Frame(width=350, height=150)
						frmB3 = Frame(width=350, height=30)
						
						frmC1 = Frame(width=200, height=30)
						frmC11= Frame(width=200, height=290)
						frmC2 = Frame(width=200, height=150)
						frmC3 = Frame(width=200, height=30)
						
						###******创建控件******###
						
						#1.Text控件
						txtMsgList = Text(frmB1)                          #frmB1表示父窗口
						#创建并配置标签tag属性
						txtMsgList.tag_config('greencolor',               #标签tag名称
											  foreground='#008C00')       #标签tag前景色，背景色为默认白色
						txtMsgList.tag_config('red',               #标签tag名称
											  foreground='#FF0000')       #标签tag前景色，背景色为默认白色
						
						txtMsg = Text(frmB2);
						txtMsg.bind("<KeyPress-Return>", sendMsgEvent)    #事件绑定，定义快捷键
						
						timeText=Text(frmC2,font=("Times", "28", "bold italic"),height=1,bg="PowderBlue")
						timeText2=Text(frmC2,fg="blue",font=("Times", "12","bold italic"))
						
						txtText=Text(frmC11,font=("Times", "11",'bold'),  #字体控制
									 width=24,height=15,                  #文本框的宽（in characters ）和高(in lines) (not pixels!)
									 spacing2=5,                          #文本的行间距
									 bd=2,                                #边框宽度
									 padx=5,pady=5,                       #距离文本框四边的距离
									 selectbackground='blue',             #选中文本的颜色
									 state=NORMAL)                        #文本框是否启用 NORMAL/DISABLED
						txtText.insert(END,'    欢迎来到超级聊天室！\n    此软件用于C/S的临时聊天软件，采用udp协议。\n    C/S分布式模式，是计算机用语。C是指Client，S是指Server。C/S模式就是指客户端/服务器模式。是计算机软件协同工作的一种模式。\n    随着计算机网络技术的成熟和应用普及，特别是局域网的发展、PC机的出现，越来越多的用户和企业开始使用计算机管理一些事务。PC机的资源没有大型、中型甚至小型主机丰富，但将多台PC机联成网，必然会增加资源含量，各个用户都在网络上来共享所有资源。\n    根据客户/服务器（Client/Server简记为C/S）体系结构的概念，至少用两台计算机来分别充当客户机和服务器角色。客户端可以是X86体系的风机或RISC体系的工作站等，而服务器端硬件一般比较高档。\n    比如：高档PC服务器或SUN专用服务器；操作系统也比较高档，比如： Windows NT和 Unix。')
						
						#2.Button控件
						btnSend = Button(frmB3, text='发 送', width = 8,cursor='heart', command=lambda:sendMsg())
						btnCancel = Button(frmB3, text='取消', width = 8,cursor='shuttle', command=cancelMsg)
						btnExit = Button(frmB3, text='退 出', width = 8,cursor='heart', command=exitMsg)
										
						
									
						#4.Scrollbar控件
						scroLianxi = Scrollbar(frmA2,width=22,cursor='pirate',troughcolor="blue") 
						  
						#5.Listbox控件
						listLianxi = Listbox(frmA2, width=22,height=16,
											   yscrollcommand = scroLianxi.set )  #连接listbox 到 vertical scrollbar
						scroLianxi.config( command = listLianxi.yview )   #scrollbar滚动时listbox同时滚动
						
						#6.Canvas控件
						imgCanvas=Canvas(frmA3,bg='ivory')
						  
						#7.Radiobutton控件
						var = IntVar()                                    #设置variable和value可以保证只有一个按钮被按下
						R1 = Radiobutton(frmA4, text="多边形", variable=var, value=1,command=Polygon)
						R2 = Radiobutton(frmA4, text="椭圆", variable=var, value=2,command=Oval)
						
						#8.Menubutton控件
						colorMenubt =  Menubutton (frmA4, text="画板颜色", relief=RAISED )
						
						#9.Menu控件
						colorMenubt.menu  =  Menu ( colorMenubt, tearoff = 0 )
						colorMenubt["menu"]  =  colorMenubt.menu
						
						colorMenubt.menu.add_checkbutton ( label="红色",command=red)
						colorMenubt.menu.add_checkbutton ( label="绿色",command=green)
						colorMenubt.menu.add_checkbutton ( label="蓝色",command=blue)
						colorMenubt.menu.add_separator()       #添加菜单分隔符
						colorMenubt.menu.add_checkbutton ( label="连续色",command=color1)
						
						#10.Scale控件
						sizeScale = Scale(frmC3,length=135,width=18,from_=10, to=35,orient=HORIZONTAL,command=fontSize,cursor='star',
										  showvalue=0,         #不显示数值
										  sliderlength=30,     #滑块的长度             
										  troughcolor='ivory') #滑动条底色
						sizeScale.set(20)                      #设置滑块的初始值
						
						#11.Label控件
						sizeLabel = Label(frmC3,width=8,height=1,bd=1, relief=RIDGE)
						nameLabel = Label(frmC1, text='   Favorite Book List',font="Times 16 bold italic")

						
						#12.Spinbox控件
						txtSpinbox = Spinbox(frmC11,width=24,command=txtlist)
						txtSpinbox.config(values=['NO.1 《超级聊天室》  顺','NO.2 《看见》  柴静','NO.3 《平凡的世界》  路遥'])
						
						###******窗口布局******###
						frmA1.grid(row=0, column=0, padx=10, pady=3)
						frmA2.grid(row=1, column=0, padx=10)
						frmA3.grid(row=2, column=0, rowspan=1)
						frmA4.grid(row=3, column=0, rowspan=1)
						
						frmB1.grid(row=0, column=1, columnspan=1, rowspan=2, padx=1, pady=3)
						frmB2.grid(row=2, column=1, columnspan=1, padx=1, pady=1)
						frmB3.grid(row=3, column=1, columnspan=1, padx=1)
						
						frmC1.grid(row=0, column=2, rowspan=1, padx=1, pady=1)
						frmC11.grid(row=1, column=2, rowspan=1, padx=1, pady=1)
						frmC2.grid(row=2, column=2, rowspan=1, padx=1, pady=1)  
						
						frmC3.grid(row=3, column=2, padx=1)
			 
						###******窗口布局******###
						#固定大小
						frmA1.grid_propagate(0)
						frmA2.grid_propagate(0)
						frmA3.grid_propagate(0)
						#frmA4.grid_propagate(0)
						
						frmB1.grid_propagate(0)
						frmB2.grid_propagate(0)
						frmB3.grid_propagate(0)
						
						frmC1.grid_propagate(0)
						frmC11.grid_propagate(0)  
						frmC2.grid_propagate(0)
						frmC3.grid_propagate(0)
						
						###******控件布局******### 
						btnSend.grid(row=0, column=0)
						btnCancel.grid(row=0, column=1)
						btnExit.grid(row=0,column=2,padx=100)
						
						nameLabel.grid()
						sizeLabel.grid(row=0,column=0)

						
						txtMsgList.grid()
						txtMsg.grid()				

						scroLianxi.grid(row=0,column=1,ipady=120)
						
						listLianxi.grid(row=0,column=0)
						imgCanvas.grid(row=0,column=0,sticky=N)
						
						colorMenubt.grid(row=0,column=0)
						
						R1.grid(row=0,column=1) 
						R2.grid(row=0,column=2) 
						
						timeText.grid(row=0,column=0)
						timeText2.grid(row=1,column=0,sticky=E+W)
						txtText.grid(row=1,column=0,pady=5)
						sizeScale.grid(row=0,column=1)
						txtSpinbox.grid(row=0,column=0)
						

						#主事件循环
						
						btn_newy()
						showtime()
						txtMsgList.after(4000,getmessage)
						
						t.mainloop()
						
			if __name__ == '__main__':
				main()
		
		def btn_new5(): #进入群聊
			window6 = tk.Toplevel(window2)
			window6.geometry('240x100')
			window6.resizable(0,0)
			
			def in_group():
				groupname = group_name.get()
				selection = "ingroup"
				client.send(selection.encode())
				date = client.recv(1024)
				if date == b"yes":
					client.send(groupname.encode())
					date = client.recv(1024)
					client.send(name.encode())
					date = client.recv(1024)
					if date == b'no':
						tk.messagebox.showwarning(message='没有此群聊')
						window6.destroy()
					if date == b'ok':
						tk.messagebox.showinfo(message='进入成功!!')
						window6.destroy()
						window2.destroy()
						
						root = Tk()
						root.title(groupname)
						root.resizable(0,0)
						#发送按钮事件
						def sendmessage():
						  #在聊天内容上方加一行 显示发送人及发送时间
						  msg = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) +'\n '+ text_msg.get('0.0', END)
						  selection = "sendgroup"
						  client.send(selection.encode())
						  date = client.recv(1024)
						  if date == b"yes":
							  client.send(name.encode())
							  date = client.recv(1024)
							  client.send(groupname.encode())
							  date = client.recv(1024)
							  client.send(msg.encode())
							  date = client.recv(1024)
							  
							  
						  text_msg.delete('0.0', END)
						  
						def showmessage():
							gi = 'yes'
							gy = 'no'
							selection = "showmessage"
							text_msglist.delete('0.0',END)
							client.send(selection.encode())
							date = client.recv(1024)
							if date == b"yes":
								client.send(groupname.encode())
								while True:
									date = client.recv(1024)
									if date == b'nomore':
										break
									else:
										Sname = date.decode()
										client.send(gi.encode())
										
										date = client.recv(1024)
										Tell = date.decode()
										text_msglist.insert(END, Sname+'  :'+Tell, 'red')
							
							text_msglist.after(10000,showmessage)			
							
						def exitmessage():
							root.destroy()
							main_window()
						 
						def sendEvent(event):
							if event.keysym == "Return":  #按回车键可发送
								sendmessage()
							
						def btn_newy():#显示用户函数
							gi = "yes"
							gp = "ok"
							selection = "groupxianshi"
							client.send(selection.encode())
							listLianxi1.delete(0,END)
							date = client.recv(1024)
							if date == b"yes":
								client.send(groupname.encode())
								date = client.recv(1024)
								client.send(gi.encode())
								while True:
									date = client.recv(1024)
									if date == b"Nomore":
										client.send(gp.encode())
										break
									else:
										nowname = date.decode()
										listLianxi1.insert(END,"在线联系人------"+nowname)
										client.send(gi.encode())	    
								
								listLianxi1.delete(0)
								
								
								
							
						 
						#创建几个frame作为容器
						frame_left_top   = Frame(width=380, height=270)
						frame_left_center  = Frame(width=380, height=100)
						frame_left_bottom  = Frame(width=380, height=26)
						frame_right     = Frame(width=170, height=270)
						
						##创建需要的几个元素
						text_msglist    = Text(frame_left_top)
						text_msg      = Text(frame_left_center);
						text_msg.bind("<KeyPress-Return>", sendEvent)    #事件绑定，定义快捷键
						button_sendmsg   = Button(frame_left_bottom, text='发送', command=sendmessage)
						button_exitmsg   = Button(frame_left_bottom, text='退出', command=exitmessage)
						
						#创建一个绿色的tag
						text_msglist.tag_config('green', foreground='#008B00')
						text_msglist.tag_config('red', foreground='#FF0000')
						
						  
						#Listbox控件
						listLianxi1 = Listbox(frame_right, width=22,height=20,)
						
						#使用grid设置各个容器位置
						frame_left_top.grid(row=0, column=0, padx=2, pady=5)
						frame_left_center.grid(row=1, column=0, padx=2, pady=5)
						frame_left_bottom.grid(row=2, column=0)
						frame_right.grid(row=0, column=1, padx=4, pady=5)
						
						frame_right.grid_propagate(0)
						frame_left_top.grid_propagate(0)
						frame_left_center.grid_propagate(0)
						frame_left_bottom.grid_propagate(0)
						
						#把元素填充进frame
						text_msglist.grid()
						text_msg.grid()
						button_sendmsg.grid(sticky=E)
						button_exitmsg.grid(row=0,column = 1,padx = 280)
						listLianxi1.grid(row=0,column=0)
						

						
						btn_newy()
						showmessage()
						#主事件循环
						root.mainloop()

						
			def d_group():
				window6.destroy()
						
				
			
			tk.Label(window6, text='请输入群聊名字： ').place(x=10, y= 10)
			group_name = tk.Entry(window6, textvariable=var_name,width=30)#创建一个`entry`，显示为变量`var_usr_name`
			group_name.place(x=10, y=40)
			group = tk.Button(window6,text='取消', width=7, command = d_group)
			group.place(x=165,y=65)
			group = tk.Button(window6,text='确定', width=7, command = in_group)
			group.place(x=10,y=65)
			
			
		def btn_new6(): #创建群聊
			window6 = tk.Toplevel(window2)
			window6.geometry('240x100')
			window6.resizable(0,0)
			
			def create_group(): #创建群聊
				groupname = group_name.get()
				selection = "creategroup"
				client.send(selection.encode())
				date = client.recv(1024)
				if date == b"yes":
					client.send(name.encode())
					date = client.recv(1024)
					client.send(groupname.encode())
					date = client.recv(1024)
					if date == b'ok':
						tk.messagebox.showinfo(message='创建成功!!')
						window6.destroy()
					else:
						tk.messagebox.showwarning(message='未知错误')
						
			def d_group():
				window6.destroy()	
			
			tk.Label(window6, text='请给你的群起一个好听的名字： ').place(x=10, y= 10)
			group_name = tk.Entry(window6, textvariable=var_name,width=30)#创建一个`entry`，显示为变量`var_usr_name`
			group_name.place(x=10, y=40)
			group = tk.Button(window6,text='取消', width=7, command = d_group)
			group.place(x=165,y=65)
			group = tk.Button(window6,text='确定', width=7, command = create_group)
			group.place(x=10,y=65)
			

			
		def btn_new7(): #删除群聊
			tk.messagebox.showwarning(message='自己创建的群聊可不能退噢！！')

		def btn_new8(): #机器人聊天室
			pass
		def btn_new9(): #习大大聊天
			tk.messagebox.showwarning(message='你觉得可能吗？？？')
		def btn_new10(): #关于我们
			window6 = tk.Toplevel(window2)
			window6.geometry('300x400')
			window6.resizable(0,0)
			
			canvas1 = tk.Canvas(window6, width=300,height=400,bd=0, highlightthickness=0)
			canvas1.create_image(80, 200,image=photo)
			canvas1.place(x=0,y=0)					
						
			la1=tk.Label(window6, text='软件名 ： Mychat')
			la2=tk.Label(window6, text='版本号 ： 1.0')
			la3=tk.Label(window6, text='功能  ：  聊天交友')
			la4=tk.Label(window6, text='制作人 ：  顺')
			la5=tk.Label(window6, text='wecome   you ！！')
			

			canvas1.create_window(87,100,width=100,window=la1)
			canvas1.create_window(87,130,width=100,window=la2)
			canvas1.create_window(87,160,width=100,window=la3)
			canvas1.create_window(87,190,width=100,window=la4)
			canvas1.create_window(87,220,width=100,window=la5)
			
		def btn_new11():#退出
				selection = "exit"
				client.send(selection.encode())
				
				date = client.recv(1024)
				window2.destroy()
				sys.exit()
			
			
			
			
		canvas = tk.Canvas(window2, width=540,height=380,bd=0, highlightthickness=0)
		
		imgpath = 'win1.gif'
		img = Image.open(imgpath)
		photo = ImageTk.PhotoImage(img)
		
		imgpath2 = 'win4.gif'
		img2 = Image.open(imgpath2)
		photo2 = ImageTk.PhotoImage(img2)
		
		
		canvas.create_image(250,270, image=photo2)
		canvas.place(x=0,y=0)
		

		btn_new4 = tk.Button(window2, text='获取信息',command=btn_new4)	
		

		
		
		
		
		mb1 = tk.Menubutton(window2, text='群聊',relief=RAISED)
		filemenu = Menu(mb1, tearoff=False)
		filemenu.add_command(label='进入群聊', command=btn_new5)
		filemenu.add_command(label='创建群聊', command=btn_new6)
		filemenu.add_separator()   #添加分割线
		filemenu.add_command(label='删除群聊', command=btn_new7)
		mb1.config(menu=filemenu)
		
		mb2 = tk.Menubutton(window2, text='进入聊天室',relief=RAISED)
		filemenu = Menu(mb2, tearoff=False)
		filemenu.add_command(label='个人超级聊天室', command=btn_new2)
		filemenu.add_command(label='机器人聊天室', command=btn_new8)
		filemenu.add_separator()   #添加分割线
		filemenu.add_command(label='和习大大聊天', command=btn_new9)
		mb2.config(menu=filemenu)
		
		
		mb3 = tk.Menubutton(window2, text='关于',relief=RAISED)
		filemenu = Menu(mb3, tearoff=False)
		filemenu.add_command(label='个人信息', command=btn_new3)
		filemenu.add_command(label='关于我们', command=btn_new10)
		filemenu.add_separator()   #添加分割线
		filemenu.add_command(label='退出登录', command=btn_new11)
		mb3.config(menu=filemenu)

			
		
		#创建Listbox
		lb = tk.Listbox(window2,font=('Helvetica',14,"bold italic"))  #将var2的值赋给Listbox
		lb.place(relwidth=0.9,relheight=0.9)
		yscrollbar = Scrollbar(lb,command=lb.yview)
		yscrollbar.pack(side=RIGHT, fill=Y)
		lb.config(yscrollcommand=yscrollbar.set)
		
		canvas.create_window(85,30,width=80,window=btn_new4)
		canvas.create_window(170,30,width=80,window=mb2)
		canvas.create_window(255,30,width=80,window=mb1)
		canvas.create_window(337,30,width=80,window=mb3)
		canvas.create_window(210,213,width=335, height=323,window=lb)
		
		btn_newx()
		window2.mainloop()#///
	
	selection = "denglu"
	name = var_name.get()
	pwd = var_pwd.get()	
	id = 0
	if name == '' or pwd == ''  :
		tk.messagebox.showwarning(message='服务器压力大，请不要输入空的账号密码')
		exit('由于你的任性，再见！')
	else:
		client.send(selection.encode())
		date = client.recv(1024)#接受数据，1024个字
		if date == b"yes":
			client.send(name.encode())
			date = client.recv(1024)
			if date == b"yes":
				client.send(pwd.encode())
				date = client.recv(1024)
				if date == b"yes":
					window.destroy()
					main_window()
				if date == b"same":
					tk.messagebox.showwarning(message='一个人只能登陆一次哟')
				else:
					tk.messagebox.showwarning(message='你傻吗？密码都能记错')
			else:
				tk.messagebox.showwarning(message='服务器出现了一点异常')
		else:
			tk.messagebox.showwarning(message='服务器异常')
		 

	



#注册函数		
def sign_up():
	def sign_to_comfirm():
		selection = "zhuce"
		newname=new_name.get()
		newpwd=new_pwd.get()
		newname1=new_name1.get()
		newschool=new_school.get()
		newmajor=new_major.get()
		newid=new_id.get()
		newclass=new_class.get()
		newpwdconfirm=new_pwd_confirm.get()
		if newname == '' or newpwd == '' or newname1 == '' or newschool == '' or newmajor == '' or newid == '' or newclass == '' :
			tk.messagebox.showerror(message='请完善所有信息，不要有所保留噢！！')
		else:
			if newpwd == newpwdconfirm :
				client.send(selection.encode())
				date = client.recv(1024)#接受数据，1024个字
				if date == b"yes":
					client.send(newname.encode())
					date1 = client.recv(1024)#接受数据，1024个字
					client.send(newpwd.encode())
					date2 = client.recv(1024)#接受数据，1024个字
					client.send(newname1.encode())
					date3 = client.recv(1024)#接受数据，1024个字
					client.send(newschool.encode())
					date4 = client.recv(1024)#接受数据，1024个字
					client.send(newmajor.encode())
					date5 = client.recv(1024)#接受数据，1024个字
					client.send(newid.encode())
					date6 = client.recv(1024)#接受数据，1024个字
					client.send(newclass.encode())
					date7 = client.recv(1024)#接受数据，1024个字
				if date7 == b"yes":
					tk.messagebox.showinfo(message='恭喜你成为超级聊天室的一员')
					window1.destroy()
				else:
					tk.messagebox.showinfo(message='这个账号有人注册过了哟')
					exit('服务器异常，请重试')
			else :
				tk.messagebox.showerror(message='你逗我呀？两次密码输入不同')
	
	tk.messagebox.showinfo(message='YES')
	window1=tk.Toplevel(window)#新的注册窗口
	window1.geometry('350x450')
	window1.title('Sign up window')
	
	new_name = tk.StringVar()#将输入的注册名赋值给变量
	tk.Label(window1, text='User name: ').place(x=10, y= 10)#将`User name:`放置在坐标（10,10）。
	entry_new_name = tk.Entry(window1, textvariable=new_name)#创建一个注册名的`entry`，变量为`new_name`
	entry_new_name.place(x=150, y=10)#`entry`放置在坐标（150,10）
	
	new_pwd = tk.StringVar()
	tk.Label(window1, text='Password: ').place(x=10, y=50)
	entry_new_pwd = tk.Entry(window1, textvariable=new_pwd, show='*')
	entry_new_pwd.place(x=150, y=50)
	
	new_pwd_confirm = tk.StringVar()
	tk.Label(window1, text='Confirm password: ').place(x=10, y= 90)
	entry_usr_pwd_confirm = tk.Entry(window1, textvariable=new_pwd_confirm, show='*')
	entry_usr_pwd_confirm.place(x=150, y=90)
	
	
	new_name1 = tk.StringVar()
	tk.Label(window1, text='name: ').place(x=10, y= 130)
	entry_new_name1 = tk.Entry(window1, textvariable=new_name1)
	entry_new_name1.place(x=150, y=130)
			
	new_school = tk.StringVar()
	tk.Label(window1, text='school: ').place(x=10, y=170)
	entry_new_school = tk.Entry(window1, textvariable=new_school)
	entry_new_school.place(x=150, y=170)
			
	new_major = tk.StringVar()
	tk.Label(window1, text='major: ').place(x=10, y= 210)
	entry_major = tk.Entry(window1, textvariable=new_major)
	entry_major.place(x=150, y=210)
			
	new_class = tk.StringVar()
	tk.Label(window1, text='class: ').place(x=10, y=250)
	entry_class = tk.Entry(window1, textvariable=new_class)
	entry_class.place(x=150, y=250)
			
	new_id = tk.StringVar()
	tk.Label(window1, text='id: ').place(x=10, y=290)
	entry_id = tk.Entry(window1, textvariable=new_id)
	entry_id.place(x=150, y=290)
	
	btn_comfirm_sign_up = tk.Button(window1, text='Sign up', command=sign_to_comfirm)
	btn_comfirm_sign_up.place(x=150, y=330)
	
	
	window1.mainloop()





def loginEvent(event):
	if event.keysym == "Return":  #按回车键可发送
		login()
	






canvas = tk.Canvas(window, height=200, width=500)#创建画布
image_file = tk.PhotoImage(file='welcome.gif')#加载图片
image = canvas.create_image(0,0, anchor='nw', image=image_file)#将图片放在画布上
canvas.grid(row=0,column=0)#上端

tk.Label(window, text='User name: ').place(x=50, y= 150)#创建一个`label`名为`User name: `置于坐标（50,150）
tk.Label(window, text='Password: ').place(x=50, y= 190)

var_name = tk.StringVar()#定义变量
entry_name = tk.Entry(window, textvariable=var_name,width=30)#创建一个`entry`，显示为变量`var_usr_name`
entry_name.place(x=160, y=150)
var_pwd = tk.StringVar()
entry_pwd = tk.Entry(window, textvariable=var_pwd, width=30,show='*')#`show`这个参数将输入的密码变为`***`的形式
entry_pwd.place(x=160, y=190)

entry_pwd.bind("<KeyPress-Return>", loginEvent)    #事件绑定，定义快捷键

btn_login = tk.Button(window, text='Login', width=8,command=login)#定义一个`button`按钮，名为`Login`,触发命令为`usr_login`
btn_login.place(x=170, y=230)
btn_sign_up = tk.Button(window, text='Sign up', width=8, command=sign_up)
btn_sign_up.place(x=300, y=230)

window.mainloop()

