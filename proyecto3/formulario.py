from tkinter import *
from tkinter import ttk
#class OptionMenu(
    #master : Misc | None,
    #variable : StringVar,
    #default : str | None = None,
    #*values : str,
    #style : str = "",
    #direction :Literal['above', 'below', 'left', 'right', 'flush'] = "below",
    #command: ((StringVar) -> object) | None = None
#)
#btn = ttk.Button(frm, ...)
#print(btn.configure().keys())
#class tkinter.Tk(screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None
root = Tk()
frm = ttk.Frame(root, padding=50)
frm.grid()
#ttk.Combobox()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Combobox.grid(column=5, row=3)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
