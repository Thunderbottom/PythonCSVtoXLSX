from tkinter import *
from tkinter.filedialog import askdirectory

class Window(Frame):
    def __init__(self, master= None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title('CSV to XLSX Converter')
        self.pack(fill=BOTH, expand = 1)

        # Enter Path
        self.pathText = Entry(self)

        # Radiobutton
        # CheckVar is used to get() value of the checkbutton during conversion
        self.CheckVar = IntVar()
        self.firstLine = Radiobutton(self, text='Use First Line as Header', variable=self.CheckVar, value=1)
        self.blankLine = Radiobutton(self, text='Use First Line as Header', variable=self.CheckVar, value=2)
        # Buttons
        convert = Button(self, text='Convert', command=self.convertFiles)
        browse = Button(self, text='Browse', command=self.browse)

        # Place entry field
        self.pathText.place(relx=0.5, rely=0.3, anchor=CENTER)

        # Place Radiobuttons
        self.firstLine.pack(anchor=W)
        self.blankLine.pack(anchor=W)

        browse.place(relx=0.5, rely=0.45, anchor=CENTER)
        convert.place(relx=0.5, rely=0.5, anchor=CENTER)


    def convertFiles(self):
        test = self.pathText.get()
        check = self.CheckVar.get()
        print(test)
        print(check)

    def browse(self):
        dirname = askdirectory(parent=root,initialdir="/",title='Please select a directory')
        if dirname:
            self.pathText.insert(0,dirname)

root = Tk()
root.geometry('400x400')
app = Window(root)
root.mainloop()
