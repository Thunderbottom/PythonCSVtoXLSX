from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.messagebox import askyesno, showerror, showinfo
import csvxlgui
import webbrowser
import os


def getFiles(path):
    returnFiles = []
    for file in os.listdir(path):
        if file.endswith(".csv"):
            returnFiles.append(file)
    return returnFiles


def deleteSource(path):
    delSrc = askyesno(
        'Information!', 'Do you want to delete the source CSV files?')
    if delSrc:
        for files in os.listdir(path):
            if files.endswith(".csv"):
                os.remove(files)

def main():
    class Window(Frame):

        def __init__(self, master=None):
            Frame.__init__(self, master)
            self.master = master
            master.minsize(width=500, height=500)
            self.pack_propagate(0)
            self.init_window()

        def init_window(self):
            self.master.title('CSV to XLSX Converter')
            self.pack(fill=BOTH, expand=1)

            # Enter Path
            self.pathText = Entry(self)

            # Checkbutton
            # CheckVar is used to get() value of the checkbutton during conversion
            self.CheckVar = IntVar()
            self.CheckVar.set(1)
            self.firstLine = Checkbutton(self, text='Use First Line as Header',
                                         variable=self.CheckVar, onvalue=1, offvalue=0, command=self.checkSet)

            # Buttons
            convert = Button(self, text='Convert', command=self.convertFiles)
            browse = Button(self, text='Browse', command=self.browse)

            # Place entry field
            self.pathText.place(relx=0.5, rely=0.20, anchor=CENTER)
            browse.place(relx=0.5, rely=0.3, anchor=CENTER)

            # Place Checkbutton
            self.firstLine.place(relx=0.5, rely=0.40, anchor=CENTER)

            convert.place(relx=0.5, rely=0.50, anchor=CENTER)

        def convertFiles(self):
            path = self.pathText.get()
            check = self.CheckVar.get()
            # print(path)
            # print(check)
            if not os.path.exists(path):
                showerror('Error: Cannot continue!',
                          'Make sure the path is valid before trying to continue')
                self.pathText.delete(0, END)
            else:
                fileList = getFiles(path)
                if not fileList:
                    showerror('Error: No CSV files found!',
                              'Make sure there are CSV files in the given path before continuing')
                    self.pathText.delete(0, END)
                else:
                    convertFile = csvxlgui.converter(path, fileList, check)

                    if convertFile:
                        info = showinfo(
                            'Information!', 'There were some errors while converting. \nPlease see error.log for more info.')
                    else:
                        info = showinfo(
                            'Success!', 'The files were converted successfully. \nFor more information please see output.log')
                        deleteSource(fileList)
                        self.pathText.delete(0, END)

        def browse(self):
            dirname = askdirectory(parent=root, initialdir="/",
                                   title='Please select a directory')
            if dirname:
                self.pathText.insert(0, dirname)

        def checkSet(self):
            if not self.CheckVar.get():
                info = showinfo(
                    'Information!', 'The first line of the output XLSX file will now be blank')

    root = Tk()
    def callback(event):
        webbrowser.open_new('https://github.com/Thunderbottom/PythonCSVtoXLSX')

    lbl = Label(root, text=r"Help & About", fg="blue", cursor="hand2")
    lbl.pack(side='bottom')
    lbl.bind("<Button-1>", callback)
    root.geometry('600x600')
    app = Window(root)
    root.mainloop()


if __name__ == '__main__':
    main()
