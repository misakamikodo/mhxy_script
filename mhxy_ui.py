from tkinter import *

if __name__ == '__main__':
    root = Tk()
    root.title("mhxy_script")
    root.geometry('300x500')
    # root.iconbitmap('mhxy.ico')

    mineButton = Button(root, text='挖矿', width=8, bg='white', activebackground='grey', activeforeground='black', font=('微软雅黑', 12))
    mineButton.pack(side = TOP, expand = NO)
    root.mainloop()
