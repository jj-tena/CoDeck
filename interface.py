from cgitb import text
import tkinter as tk
from webbrowser import get

from sqlalchemy import true

app = tk.Tk()
app.geometry("900x900")
app.configure(background="#30323D")
app.title("CoDeck")

tk.Label(
    app, 
    text="CoDeck Keys Selector", 
    background="#5C80BC",
    font=("Ubuntu Mono",26)
    ).pack(fill=tk.BOTH, expand=True)


def create_script_selector(number):
    script_frame = tk.Frame(app, height=10, padx=30, pady=15)
    script_frame.pack(fill="both", expand=True)

    path1 = tk.StringVar(app)

    tk.Label(
        script_frame,
        text="Script "+str(number) + " path",
        font=("Ubuntu Mono",12)
        ).pack(side="left", padx=10)

    tk.Button(
        script_frame,
        background="#5C80BC",
        activebackground="#3B5B91",
        activeforeground="#FFFFFF",
        borderwidth=0,
        text="Find",
        font=("Ubuntu Mono",10),
        command=lambda: print(path1.get())
    ).pack(side="left")

    tk.Button(
        script_frame,
        text="Save",
        background="#F9627D",
        activebackground="#F7264D",
        activeforeground="#FFFFFF",
        borderwidth=0,
        width=7,
        font=("Ubuntu Mono",10),
        command=lambda: print(path1.get())
    ).pack(side="right")

    tk.Entry(
        script_frame,
        background="#4D5061",
        foreground="#FFFFFF",
        textvariable=path1,
        width=52,
        borderwidth=0,
        font=("Ubuntu Mono",12),
    ).pack(side="right", expand=True)

   


for i in range(0, 8):
    create_script_selector(i+1)


app.mainloop()
