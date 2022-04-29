from cgitb import text
import tkinter as tk
from tkinter import N, filedialog
from webbrowser import get

import database
        
def browse_files(path, number):
    filename = filedialog.askopenfilename(
        initialdir="./",
        title="Select a File",
        filetypes=(
            ("Python files", "*.py*"),
            ("all files", "*.*")
        )
    )

    print(filename)

    database.updateRow(number, filename)

    # Change runtime variable to notify the user that the path has
    # been selected correctly
    path.set(filename)


def save_path(path, number):

    print(path)

    database.updateRow(number, path)


def create_input(app, number):

    # Create frame to store the widgets
    script_frame = tk.Frame(app, height=10, padx=30, pady=15)
    script_frame.pack(fill="both", expand=True)


    
    # Variable to store the path on runtime
    path = tk.StringVar(
        app, value=database.getPath(number))

    # print(database.readRow(nunb))

    # Create widgets
    create_label(script_frame,number)
    create_button(script_frame, "#5C80BC", "#3B5B91", "left",
                  "Find", lambda: browse_files(path, number))
    create_button(script_frame, "#F9627D", "#F7264D", "right",
                  "Save", lambda: save_path(path.get(), number))
    create_entry(script_frame, path)

def create_label(frame, number):
    tk.Label(
        frame,
        text=f'Script {number} path',
        font=("Ubuntu Mono", 12)
    ).pack(side="left", padx=10)

def create_button(frame, bg_color, fg_color, side, text, funct_call):
    tk.Button(
        frame,
        background=bg_color,
        activebackground=fg_color,
        activeforeground="#FFFFFF",
        borderwidth=0,
        text=text,
        font=("Ubuntu Mono", 10),
        command=funct_call
    ).pack(side=side)

def create_entry(frame, path):
    tk.Entry(
        frame,
        background="#4D5061",
        foreground="#FFFFFF",
        textvariable=path,
        width=52,
        borderwidth=0,
        font=("Ubuntu Mono", 12),
    ).pack(side="right", expand=True)

def create_title(app):
    tk.Label(
        app,
        text="CoDeck Keys Selector",
        background="#5C80BC",
        font=("Ubuntu Mono", 26)
    ).pack(fill=tk.BOTH, expand=True)

def setup_interface():
    app = tk.Tk()
    app.geometry("900x900")
    app.configure(background="#30323D")
    app.title("CoDeck")
    return app

def main():
    app = setup_interface()
    create_title(app)
  
    for i in range(0, 8):
        create_input(app, i+1)

    app.mainloop()

if __name__ == "__main__":
    main()
