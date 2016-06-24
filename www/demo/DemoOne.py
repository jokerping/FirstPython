#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'第一个Python文件'
from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel=Label(self,text='HelloWorld')
        self.helloLabel.pack()
        self.button=Button(self,text='Quit',command=self.hello)
        self.button.pack()
        self.input=Entry(self)
        self.input.pack()

    def hello(self):
        name=self.input.get() or 'world'
        messagebox.showinfo('Message','Hello,%s' % name)



app = Application()
app.master.title('Hello,World')
app.mainloop()
