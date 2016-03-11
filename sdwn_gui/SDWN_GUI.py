#coding=utf-8
import os
import tkMessageBox
import matplotlib.pyplot as plt
from ttk import *
from Tkinter import *
from PIL import Image, ImageTk

class SDWN_GUI():
    def __init__(self):
        self.path = os.getcwd()
    
    def creat_widgets(self):
        
        #主窗口
        self.root = Tk()
        self.root.title(u"基于软件定义网络的无线局域网管理系统 - 重庆邮电大学")
        
        #添加主要控件
        self.top_frame = Frame(self.root)
        self.top_frame.grid(row=0)
        
        self.menu_bar = Menu(self.root)
        self.root.config(menu=self.menu_bar)
        
        self.main_frame = Frame(self.root)
        self.main_frame.grid(row=1)
        
        #--------------------------------------------------------------------------------------------
        
        #为top_frame添加三个主要控件
        self.controller_manager = Frame(self.top_frame)
        self.controller_manager.grid(row=0, column=0, padx=5)
        
        self.flow_table_manager = Frame(self.top_frame)
        self.flow_table_manager.grid(row=0, column=1, padx=5)
        
        self.load_balance_manger = Frame(self.top_frame)
        self.load_balance_manger.grid(row=0, column=2, padx=5)
        
        
        
        
        #为顶部menu_bar添加选项
        self.about_menu = Menu(self.menu_bar, tearoff=0)
        self.about_menu.add_command(label=u"关于", command=self.about_info)
        
        self.menu_bar.add_cascade(label=u"关于", menu=self.about_menu)
        
        
        
        #controller_manager增加按键
        self.user_button_img = Image.open(self.path + '/img/user.ico')
        self.user_button_photo=ImageTk.PhotoImage(self.user_button_img)
        self.user_button = Button(self.controller_manager, text=u"用户管理", image=self.user_button_photo, compound=TOP)
        
        self.ap_button_img = Image.open(self.path + '/img/ap.ico')
        self.ap_button_photo = ImageTk.PhotoImage(self.ap_button_img)
        self.ap_button = Button(self.controller_manager, text=u"AP管理", image=self.ap_button_photo, compound=TOP)
        
        self.topo_img = Image.open(self.path + '/img/topo.ico')
        self.topo_photo = ImageTk.PhotoImage(self.topo_img)
        self.topo_button = Button(self.controller_manager, text="拓扑管理", image=self.topo_photo, compound=TOP)
        
        self.controller_manager_label = Label(self.controller_manager, text=u"控制器管理")
        
        self.user_button.grid(row=0, column=0, padx=1)
        self.ap_button.grid(row=0, column=1, padx=1)
        self.topo_button.grid(row=0, column=2,padx=1)
        self.controller_manager_label.grid(row=1, columnspan=3)

        #为flow_table_manager添加按键
        self.set_flow_img = Image.open(self.path + '/img/set_flow.ico')
        self.set_flow_photo = ImageTk.PhotoImage(self.set_flow_img)
        self.set_flow_button = Button(self.flow_table_manager, text=u"配置流表", image=self.set_flow_photo, compound=TOP)
        
        self.view_flow_img = Image.open(self.path + '/img/view_flow.ico')
        self.view_flow_photo = ImageTk.PhotoImage(self.view_flow_img)
        self.view_flow_button = Button(self.flow_table_manager, text=u"查看流表", image=self.view_flow_photo, compound=TOP)        
        
        
        self.flow_table_manager_label = Label(self.flow_table_manager, text=u"流表管理")
        
        self.set_flow_button.grid(row=0, column=0, padx=1)
        self.view_flow_button.grid(row=0, column=1, padx=1)
        self.flow_table_manager_label.grid(row=1, columnspan=2)
        
        #为load_balance_manager添加按键
        self.load_balance_img = Image.open(self.path + '/img/load_balance.ico')
        self.load_balance_photo = ImageTk.PhotoImage(self.load_balance_img)
        self.load_balance_button = Button(self.load_balance_manger, text=u"负载均衡", image=self.load_balance_photo, compound=TOP)
        
        self.real_time_load_img = Image.open(self.path + '/img/real_time_load.ico')
        self.real_time_load_photo = ImageTk.PhotoImage(self.real_time_load_img)
        self.real_time_load_button = Button(self.load_balance_manger, text=u"实时负载", image=self.real_time_load_photo, compound=TOP)        
        
        self.load_balance_label = Label(self.load_balance_manger, text=u"负载管理")
        
        
        self.load_balance_button.grid(row=0, column=0, padx=1)
        self.real_time_load_button.grid(row=0, column=1, padx=1)
        self.load_balance_label.grid(row=1, columnspan=2)
        
        #退出系统按键
        self.exit_system_img = Image.open(self.path + '/img/exit_system.ico')
        self.exit_system_photo = ImageTk.PhotoImage(self.exit_system_img)
        self.exit_system_button = Button(self.top_frame, text=u"退出系统", image=self.exit_system_photo, compound=TOP)
        
        self.exit_system_button.grid(row=0, column=3, rowspan=2)
        
        
        #--------------------------------------------------------------------------------------------
        #为main_frame添加两个控件
        self.usual_use_frame = Frame(self.main_frame, height=800, width=800)
        self.show_pic_frame = Frame(self.main_frame, height=800, width=600)
        
        
        
        
        self.usual_use_frame.grid(row=0, column=0, sticky="N")
        self.show_pic_frame.grid(row=0, column=1, sticky="N")
        
        #为self.usual_use_frame添加菜单
        self.usual_use_label = Label(self.usual_use_frame, text=u"    常用操作    ", pady=10)
        self.add_flow_button = Button(self.usual_use_frame, text=u"   添加流表   ")
        self.delete_flow_button = Button(self.usual_use_frame, text=u"   删除流表   ")
        self.add_lan_load_button = Button(self.usual_use_frame, text=u"有线交换网络实时负载")
        self.add_wlan_load_button = Button(self.usual_use_frame, text=u"无线交换网络实时负载")
        
 
        self.usual_use_label.grid(row=0,column=0, sticky="N")
        self.add_flow_button.grid(row=1,column=0, sticky="N")
        self.delete_flow_button.grid(row=2, column=0, sticky="N")
        self.add_lan_load_button.grid(row=3, column=0, sticky="N")
        self.add_wlan_load_button.grid(row=4, column=0, sticky="N")
        
        #引入matplotlib生成系统实时负载图
        
        #程序进入主循环
        
        self.root.mainloop()
        
    def about_info(self):
        aboutStr = "基于软件定义网络的无线局域网管理系统 - 重庆邮电大学\n V1.0"
        tkMessageBox.showinfo("关于", aboutStr)    
        
        
if __name__ == "__main__":
    gui = SDWN_GUI()
    gui.creat_widgets()
        