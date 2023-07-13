from tkinter import *

from GIF_module import GIF     #import file

root=Tk()
root.geometry('800x400')
label=label(root)
label.place(x=0,y=0)


GIF(root,label,speed=3,file_name='1.gif',loops=1)





root.mainloop()