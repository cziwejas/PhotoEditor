from customtkinter import *
import mix

win = CTk()

def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)

combobox = CTkComboBox(master=win,
                                     values=["option 1", "option 2"],
                                     command=combobox_callback)
combobox.pack(padx=20, pady=10)

win.mainloop()