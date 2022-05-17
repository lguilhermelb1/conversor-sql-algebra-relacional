import tkinter as tk
from tkinter import simpledialog, Label
from PIL import Image, ImageTk

ROOT = tk.Tk()

ROOT.withdraw()


def consulta():
    # dialog
    entrada = simpledialog.askstring(title="Conversor",
                                     prompt="Insira a consulta:")

    return entrada


def resultado():
    img = tk.PhotoImage(file='teste.png')
    Label(ROOT, image=img).pack()
    ROOT.mainloop()
