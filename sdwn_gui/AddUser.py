#coding=utf-8
import os
import tkMessageBox
import matplotlib.pyplot as plt
from ttk import *
from Tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("添加新用户")

main_frame = Frame(root)
main_frame.grid(sticky=W)

device_id_label = Label(main_frame, text=u"终端ID：", width=15)
device_name_label = Label(main_frame, text=u"终端名：", width=15)
device_mac_label = Label(main_frame, text=u"终端MAC地址：", width=15)

clean_button = Button(main_frame, text=u"重置", width=10)
confirm_button = Button(main_frame, text=u"确认", width=10)

device_id_text = Entry(main_frame, width=20)
device_name_text = Entry(main_frame, width=20)
device_mac_text = Entry(main_frame, width=20)

device_id_label.grid(row=0, column=0, padx=3, pady=10, sticky=W)
device_name_label.grid(row=1, column=0, padx=3, pady=10, sticky=W)
device_mac_label.grid(row=2, column=0, padx=3, pady=10, sticky=W)

device_id_text.grid(row=0, column=1, padx=3, sticky=E)
device_name_text.grid(row=1, column=1, padx=3, sticky=E)
device_mac_text.grid(row=2, column=1, padx=3, sticky=E)

clean_button.grid(row=3, column=0)
confirm_button.grid(row=3, column=1)

root.mainloop()