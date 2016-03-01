#coding=utf-8
from Tkinter import *
import os

class SDWN_GUI():
    def __init__(self):
        self.path = os.getcwd()
        print self.path
    
    def creat_widgets(self):
        
        #主窗口
        root = Tk()
        root.title(u"基于软件定义网络的无线局域网管理系统")
        
        top_frame = Frame(root)
        top_frame.grid()
        
        photo=PhotoImage(file=self.path + '/1.gif')
        wifi_button = Label(top_frame, text="WIFI", image=photo)
        
        wifi_button.grid()
        
        
        #程序进入主循环
        root.mainloop()
        
        
if __name__ == "__main__":
    gui = SDWN_GUI()
    gui.creat_widgets()
        