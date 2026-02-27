import tkinter as tk
from tkinter import messagebox


def get_button(window, text, color, command, fg="white"):
    button = tk.Button(window, text=text, activebackground="black",
                    activeforeground="white", bg=color, fg=fg,
            command=command, height=2, width=20, font=("Helvetica bold", 20))

    return button


def get_img_label(window):
    label = tk.Label(window)
    label.grid(row=0, column=0)
    return label


def get_text_label(window, text):
    label = tk.Label(window, text=text, font=("Arial", 12))
    label.grid(row=1, column=0)
    return label


def get_entry_text(window):
    input_txt = tk.Text(
        window, height=2, width=20, font=("Helvetica bold", 15)
    )
    return input_txt


def msg_box(title, description):
    messagebox.showinfo(title, description)
