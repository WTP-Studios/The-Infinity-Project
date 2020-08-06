from tkinter import *
import tkinter.messagebox as messagebox
import speech

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.tiplabel = Label(self, text='"输入"小猪是屑",退出该程序')
        self.tiplabel.pack()
        self.valueInput = Entry(self)
        self.valueInput.pack()
        self.alertButton = Button(self, text="验证", command=self.proof)
        self.alertButton.pack()

    def proof(self):
        keyvalue = self.valueInput.get()

        if keyvalue == "小猪是屑":
            messagebox.showinfo('提示', '你说的特别对!')
            speech.say("你说的特别对!小猪真的是个屑!")
            root.destroy()
        else:
            messagebox.showerror('错误','我觉得你可以考虑一下')

def callback():
    messagebox.showwarning('警告','请回答问题!')

root = Tk()
root.geometry('300x150')
app = Application().pack()
root.protocol("WM_DELETE_WINDOW", callback)
root.mainloop()