#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter
from tkinter.filedialog import *

from lang import *

fenX = 300
fenY = 300

class GuiTk(tkinter.Tk):

    def __init__(self):
        tkinter.Tk.__init__(self)
        self.minsize(width=fenX, height=fenY)
        self.configure(background="black")
        self.grid()
        self.resizable(True, True)
        self.update()
        self.geometry(self.geometry())

        fenTrad = tkinter.Frame(self, bg="black")
        fenTrad.grid(column=1, row=0, padx=1, pady=1, sticky="nsew")

        Label(fenTrad, text=Hello_World, fg="white", bg="black", wraplength=200, anchor="center", justify="center").grid(column=0, row=0, padx=0, pady=1, sticky="nsew")
        Label(fenTrad, text=It_s_a_sentence, fg="white", bg="black", wraplength=200, anchor="center", justify="center").grid(column=0, row=1, padx=0, pady=1, sticky="nsew")
        Label(fenTrad, text=To_be_translated, fg="white", bg="black", wraplength=200, anchor="center", justify="center").grid(column=0, row=2, padx=0, pady=1, sticky="nsew")

        bouFR = Button(fenTrad, borderwidth=1, text="trad_FR", command=trad_FR, fg="white", bg="black", activebackground="white") #Traduire en FR
        bouFR.grid(column=0, row=4, padx=1, pady=1, sticky="nsew")
        bouEN = Button(fenTrad, borderwidth=1, text="trad_EN", command=trad_EN, fg="white", bg="black", activebackground="white") #Traduire en EN
        bouEN.grid(column=1, row=4, padx=1, pady=1, sticky="nsew")
    


if __name__ == "__main__":
    app = GuiTk()
    app.mainloop()