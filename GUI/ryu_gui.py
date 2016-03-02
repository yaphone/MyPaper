#coding=utf-8

from Tkinter import *

class ControllerGui():
    def __init__(self):
        self.createWidgets()
        print "Hello"
        
        
    def createWidgets(self):
        root = Tk()
        root.title("基于软件定义网络的无线局域网架构")
        
        
#        funcFrame = Frame(root).grid(row=0, column=0)
#        dispFram = Frame(root).grid(row=0, column=1)
        
        root.mainloop()
        
        
        
if __name__ == "__main__":
#    print "Hello"
    ryuGui = ControllerGui()