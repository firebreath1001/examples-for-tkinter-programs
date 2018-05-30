from tkinter import *
from tkinter import messagebox

window =Tk()



def function_name():
    messagebox.showinfo("Title",'Message Text')

B = Button(window, text ="Button Text", command =function_name )

B.pack()
window.mainloop()      #helps the window to stay on the screen for longer time
