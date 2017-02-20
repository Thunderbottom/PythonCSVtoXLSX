from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.messagebox import askyesno, showerror, showinfo
import webbrowser
import os

class Window(Frame):
    def __init__(self, master= None):
        Frame.__init__(self, master)
        self.master = master
        master.minsize(width=500, height=500)
        self.pack_propagate(0)
        self.init_window()

    def init_window(self):
        self.master.title('CSV to XLSX Converter')
        self.pack(fill=BOTH, expand = 1)

        # Enter Path
        self.pathText = Entry(self)

        # Checkbutton
        # CheckVar is used to get() value of the checkbutton during conversion
        self.CheckVar = IntVar()
        self.CheckVar.set(1)
        self.firstLine = Checkbutton(self, text='Use First Line as Header', variable=self.CheckVar, onvalue=1, offvalue=0)


        # Buttons
        convert = Button(self, text='Convert', command=self.convertFiles)
        browse = Button(self, text='Browse', command=self.browse)

        # Place entry field
        self.pathText.place(relx=0.5,rely=0.20, anchor=CENTER)
        browse.place(relx=0.5,rely=0.3, anchor=CENTER)

        # Place Checkbutton
        self.firstLine.place(relx=0.5,rely=0.40, anchor=CENTER)

        convert.place(relx=0.5, rely=0.50, anchor=CENTER)


    def convertFiles(self):
        path = self.pathText.get()
        check = self.CheckVar.get()
        #print(path)
        #print(check)
        if not os.path.exists(path):
            makeDir = askyesno('Error: Path not found!', 'The path you entered is invalid, do you want to make a directory?')
            #print(makeDir)
            if makeDir:
                os.makedirs(path)
                #TODO: checkbutton value warning
            else:
                showerror('Error: Cannot continue!', 'Make sure the path is valid before trying to continue')
                self.pathText.delete(0,END)

    def browse(self):
        dirname = askdirectory(parent=root,initialdir="/",title='Please select a directory')
        if dirname:
            self.pathText.insert(0,dirname)

root = Tk()

def callback(event):
    webbrowser.open_new('https://github.com/Thunderbottom')

lbl = Label(root, text=r"About", fg="blue", cursor="hand2")
lbl.pack(side='bottom')
lbl.bind("<Button-1>", callback)
root.geometry('600x600')
app = Window(root)
root.mainloop()
