#coding=utf-8
import os
import tkMessageBox
from ttk import *
from Tkinter import *
from PIL import Image, ImageTk

class SDWN_GUI():
    def __init__(self):
        self.path = os.getcwd()
        print self.path
    
    def creat_widgets(self):
        
        #主窗口
        self.root = Tk()
        self.root.title(u"基于软件定义网络的无线局域网管理系统 - 重庆邮电大学")
        
        #添加主要控件
        self.top_frame = Frame(self.root)
        self.menu_bar = Menu(self.root)
        
        
        self.top_frame.grid()
        
        
        #为顶部menu_bar添加选项
        self.about_menu = Menu(self.menu_bar, tearoff=0)
        self.about_menu.add_command(label=u"关于", command=self.about_info)
        
        self.menu_bar.add_cascade(label=u"关于", menu=self.about_menu)
        
        self.root.config(menu=self.menu_bar)
        
        #top_frame增加按键
        self.user_button_img = Image.open(self.path + '/img/user.ico')
        self.user_button_photo=ImageTk.PhotoImage(self.user_button_img)
        self.user_button = Button(self.top_frame, text=u"用户管理", image=self.user_button_photo, compound=TOP)
        
        self.ap_button_img = Image.open(self.path + '/img/ap.ico')
        self.ap_button_photo = ImageTk.PhotoImage(self.ap_button_img)
        self.ap_button = Button(self.top_frame, text=u"AP管理", image=self.ap_button_photo, compound=TOP)
        
        
        
        
        self.user_button.grid(row=0, column=0, padx=5)
        self.ap_button.grid(row=0, column=1, padx=5)

        
        #程序进入主循环
        self.root.mainloop()
        
    def about_info(self):
        aboutStr = "基于软件定义网络的无线局域网管理系统 - 重庆邮电大学\n V1.0"
        tkMessageBox.showinfo("关于", aboutStr)    
        
        
if __name__ == "__main__":
    gui = SDWN_GUI()
    gui.creat_widgets()
        