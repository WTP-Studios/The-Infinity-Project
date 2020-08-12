from tkinter import *
import tkinter.messagebox as messagebox
import speech

class Application(Frame):
    def __init__(self, master=None):
        Frmae.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.tiplabel = Label(self, text="XD")
        self.tiplabel.pack()
        self.valueInput = Entry(self)
        self.valueInput.pack()
        self.alertButton = Button(self, text="验证", command=self.proof)
        self.alertButton.pack()

    def proof(self):
        keyvalue = self.valueInput.get()

        if keyvalue == "?":    
            messagebox.showinfo('x', 'x')
            root.destroy()

        else:
            messagebox.showinfo('0', '0')

def callback():
    messagebox.showwarning('x', 'x')

root = Tk()
root.geometry("200x100")
app = Application().pack()
root.protocol("WM_DELETE_WINDOW", callback)
root.mainloop()    
